import logging
import pprint
# The following setup of logging needs to happen before everything else
from plenum.common.util import getlogger, setupLogging, DISPLAY_LOG_LEVEL, \
    DemoHandler
from ioflo.aid.consoling import Console

from anoncreds.protocol.types import AttribsDef, AttribType
from anoncreds.protocol.verifier import verify_proof
from anoncreds.temp_primes import P_PRIME, Q_PRIME


def out(record, extra_cli_value=None):
    """
    Callback so that this cli can manage colors

    :param record: a log record served up from a custom handler
    :param extra_cli_value: the "cli" value in the extra dictionary
    :return:
    """
    logger.display(record.msg)


logging.root.addHandler(DemoHandler(out))
logging.root.handlers = []
setupLogging(DISPLAY_LOG_LEVEL,
             Console.Wordage.mute)
logger = getlogger("test_anon_creds")

from anoncreds.protocol.attribute_repo import InMemoryAttributeRepo
from anoncreds.protocol.proof import Proof

from plenum.common.txn import DATA
from plenum.common.txn import TXN_TYPE
from plenum.test.helper import genHa
from sovrin.common.txn import CRED_DEF
from sovrin.common.util import getCredDefTxnData
from sovrin.test.helper import genTestClient, submitAndCheck

BYU = AttribsDef('BYU',
                 [AttribType("first_name", encode=True),
                  AttribType("last_name", encode=True),
                  AttribType("birth_date", encode=True),
                  AttribType("expire_date", encode=True),
                  AttribType("undergrad", encode=True),
                  AttribType("postgrad", encode=True)]
                 )

attributes = BYU.attribs(
    first_name="John",
    last_name="Doe",
    birth_date="1970-01-01",
    expire_date="2300-01-01",
    undergrad="True",
    postgrad="False"
)

attrNames = tuple(attributes.keys())


def testAnonCredFlow(looper, tdir, nodeSet, issuerSigner, proverSigner,
                     verifierSigner, addedIPV):
    # 3 Sovrin clients acting as Issuer, Signer and Verifier
    issuer = genTestClient(nodeSet, tmpdir=tdir, signer=issuerSigner,
                           peerHA=genHa())
    prover = genTestClient(nodeSet, tmpdir=tdir, signer=proverSigner,
                           peerHA=genHa())
    verifier = genTestClient(nodeSet, tmpdir=tdir, signer=verifierSigner,
                             peerHA=genHa())

    looper.add(issuer)
    looper.add(prover)
    looper.add(verifier)
    looper.run(issuer.ensureConnectedToNodes(),
               prover.ensureConnectedToNodes(),
               verifier.ensureConnectedToNodes())
    # Adding signers
    issuer.signers[issuerSigner.identifier] = issuerSigner
    logger.display("Key pair for Issuer created \n"
                   "Public key is {} \n"
                   "Private key is stored on disk\n".format(
        issuerSigner.verstr))
    prover.signers[proverSigner.identifier] = proverSigner
    logger.display("Key pair for Prover created \n"
                   "Public key is {} \n"
                   "Private key is stored on disk\n".format(
        proverSigner.verstr))
    verifier.signers[verifierSigner.identifier] = verifierSigner
    logger.display("Key pair for Verifier created \n"
                   "Public key is {} \n"
                   "Private key is stored on disk\n".format(
        verifierSigner.verstr))

    # TODO BYU.name is used here instead of issuerSigner.identifier due to
    #  tight coupling in Attribs.encoded()
    issuerId = BYU.name
    proverId = proverSigner.identifier
    # Issuer's attribute repository
    attrRepo = InMemoryAttributeRepo()
    attrRepo.attributes = {proverId: attributes}
    issuer.attributeRepo = attrRepo
    name1 = "Qualifications"
    version1 = "1.0"
    ip = issuer.peerHA[0]
    port = issuer.peerHA[1]
    interactionId = 'LOGIN-1'

    # Issuer publishes credential definition to Sovrin ledger
    credDef = issuer.newCredDef(attrNames, name1, version1,
                                p_prime=P_PRIME, q_prime=Q_PRIME,
                                ip=ip, port=port)
    # issuer.credentialDefinitions = {(name1, version1): credDef}
    logger.display("Issuer: Creating version {} of credential definition"
                   " for {}".format(version1, name1))
    print("Credential definition: ")
    pprint.pprint(credDef.get())  # Pretty-printing the big object.
    op = {TXN_TYPE: CRED_DEF, DATA: getCredDefTxnData(credDef)}
    logger.display("Issuer: Writing credential definition to "
                   "Sovrin Ledger...")
    submitAndCheck(looper, issuer, op, identifier=issuerSigner.identifier)

    # Prover requests Issuer for credential (out of band)
    logger.display("Prover: Requested credential from Issuer")
    # Issuer issues a credential for prover
    logger.display("Issuer: Creating credential for "
                   "{}".format(proverSigner.verstr))

    encodedAttributes = attributes.encoded()
    revealedAttrs = ["undergrad"]
    pk = {
        issuerId: prover.getPkFromCredDef(credDef)
    }
    proof = Proof(pk)
    proofId = proof.id
    prover.proofs[proofId] = proof
    cred = issuer.createCredential(proverId, name1, version1,
                                   proof.U[issuerId])
    logger.display("Prover: Received credential from "
                   "{}".format(issuerSigner.verstr))

    # Prover intends to prove certain attributes to a Verifier
    # Verifier issues a nonce
    logger.display("Prover: Requesting Nonce from verifier…")
    logger.display("Verifier: Nonce received from prover"
                   " {}".format(proverId))
    nonce = verifier.generateNonce(interactionId)
    logger.display("Verifier: Nonce sent.")
    logger.display("Prover: Nonce received")

    presentationToken = {
        issuerId: (
            cred[0], cred[1],
            proof.vprime[issuerId] + cred[2])
    }
    # Prover discovers Issuer's credential definition
    logger.display("Prover: Preparing proof for attributes: "
                   "{}".format(revealedAttrs))
    proof.setParams(encodedAttributes, presentationToken,
                    revealedAttrs, nonce)
    prf = Proof.prepareProof(pk_i=proof.pk_i, masterSecret=proof.masterSecret,
                             credential=presentationToken,
                             attrs=attributes.encoded(),
                             revealedAttrs=revealedAttrs,
                             nonce=nonce)
    logger.display("Prover: Proof prepared.")
    logger.display("Prover: Proof submitted")
    logger.display("Verifier: Proof received.")
    logger.display("Verifier: Looking up Credential Definition"
                   " on Sovrin Ledger...")

    # Verifier fetches the credential definition from ledger
    verifier.credentialDefinitions = {
        (issuerId, name1, version1): credDef
    }
    verified = verify_proof(pk, prf, nonce,
                            attributes.encoded(),
                            revealedAttrs)
    # Verifier verifies proof
    logger.display("Verifier: Verifying proof...")
    logger.display("Verifier: Proof verified.")
    assert verified
    logger.display("Prover: Proof accepted.")
