import pytest

from plenum.client.signer import SimpleSigner
from plenum.test.plugin.helper import getPluginPath

from sovrin.common.txn import TXN_TYPE, TARGET_NYM, TXN_ID, ROLE
from sovrin.common.txn import STEWARD, NYM, SPONSOR
from sovrin.test.helper import TestNodeSet,\
    genTestClient, createNym, addUser

from plenum.test.conftest import getValueFromModule

from plenum.test.conftest import tdir, looper, counter, unstartedLooper, \
    nodeReg, up, ready, keySharedNodes, whitelist, logcapture


@pytest.fixture(scope="module")
def allPluginsPath():
    return [getPluginPath('stats_consumer')]


@pytest.fixture(scope="module")
def stewardSigner():
    seed = b'is a pit a seed, or somepin else'
    signer = SimpleSigner(seed=seed)
    assert signer.verstr == 'OP2h59vBVQerRi6FjoOoMhSTv4CAemeEg4LPtDHaEWw='
    return signer


@pytest.fixture(scope="module")
def sponsorSigner():
    seed = b'sponsors are people too.........'
    signer = SimpleSigner(seed=seed)
    return signer


@pytest.fixture(scope="module")
def genesisTxns(stewardSigner):
    nym = stewardSigner.verstr
    return [{
        TXN_TYPE: NYM,
        TARGET_NYM: nym,
        TXN_ID: "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
        ROLE: STEWARD
    },]

@pytest.yield_fixture(scope="module")
def nodeSet(request, tdir, nodeReg, allPluginsPath):
    primaryDecider = getValueFromModule(request, "PrimaryDecider", None)
    with TestNodeSet(nodeReg=nodeReg, tmpdir=tdir,
                     primaryDecider=primaryDecider,pluginPaths=allPluginsPath) as ns:
        yield ns


@pytest.fixture(scope="module")
def genned(nodeSet, genesisTxns):
    for n in nodeSet:
        n.addGenesisTxns(genesisTxns)
    return nodeSet


@pytest.fixture(scope="module")
def startedNodes(nodeSet, looper):
    for n in nodeSet:
        n.start(looper.loop)
    return nodeSet


@pytest.fixture(scope="module")
def client1Signer():
    seed = b'client1Signer secret key........'
    signer = SimpleSigner(seed=seed)
    assert signer.verstr == 'TuIpuBcx6P4S0Ez5LUr3HVpWERVHK56XONixonwcAf4='
    return signer


@pytest.fixture(scope="module")
def client1(client1Signer, looper, nodeSet, tdir, up):
    client = genTestClient(nodeSet, signer=client1Signer, tmpdir=tdir)
    looper.add(client)
    looper.run(client.ensureConnectedToNodes())
    return client


@pytest.fixture(scope="module")
def userSignerA(genned, addedSponsor, sponsorSigner, looper, sponsor):
    return addUser(looper, sponsor, sponsorSigner, 'userA')


@pytest.fixture(scope="module")
def userSignerB(genned, addedSponsor, sponsorSigner, looper, sponsor):
    return addUser(looper, sponsor, sponsorSigner, 'userB')


@pytest.fixture(scope="module")
def steward(looper, nodeSet, tdir, up, stewardSigner):
    s = genTestClient(nodeSet, signer=stewardSigner, tmpdir=tdir)
    for node in nodeSet:
        node.whitelistClient(s.name)
    looper.add(s)
    looper.run(s.ensureConnectedToNodes())
    return s


@pytest.fixture(scope="module")
def updatedSteward(steward):
    steward.requestPendingTxns()


@pytest.fixture(scope="module")
def sponsor(looper, nodeSet, tdir, up, steward, sponsorSigner):
    s = genTestClient(nodeSet, signer=sponsorSigner, tmpdir=tdir)
    for node in nodeSet:
        node.whitelistClient(s.name)
    looper.add(s)
    looper.run(s.ensureConnectedToNodes())
    return s


@pytest.fixture(scope="module")
def addedSponsor(genned, steward, stewardSigner, looper, sponsorSigner):
    createNym(looper, sponsorSigner.verstr, steward, stewardSigner, SPONSOR)
    return sponsorSigner
