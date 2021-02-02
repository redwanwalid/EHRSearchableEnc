import pickle
from charm.core.engine.util import objectToBytes, bytesToObject
from charm.toolbox.pairinggroup import *
from charm.toolbox.secretutil import SecretUtil
import sys
import re
import pdb
from charm.toolbox.symcrypto import AuthenticatedCryptoAbstraction, SymmetricCryptoAbstraction

try:
    from charm.core.math.pairing import G1, G2, pair, ZR, GT, hashPair as extractor
except Exception as err:
    print(err)
    exit(-1)

group = PairingGroup('SS512')

util = SecretUtil(group, False)
H = lambda x: group.hash(x, G2)
F = lambda x: group.hash(x, G2)


def pickleDump(bytes, fileName):
    pickle.dump(bytes, open(fileName, 'wb'))


def pickleLoad(pickelFile):
    return pickle.load(pickelFile)


def obToBy(dic):
    return objectToBytes(dic, group)


def byToOb(bytes):
    return bytesToObject(bytes, group)


def readFile(fileName):
    readF = open(fileName, 'rb')
    return readF


def checkPickle():
    readFile = open(sys.argv[2], 'rb')
    dic = pickle.load(readFile)
    print(dic)
    print(bytesToObject(dic, group))

def setup():
    g1 = group.random(G1)
    g2 = group.random(G2)
    egg = pair(g1, g2)
    gpWithoutHF = {'g1': g1, 'g2': g2, 'egg': egg}
    return gpWithoutHF


def authSetup(readFileGP, authName):
    pickelFileGP = pickleLoad(readFileGP)
    gp = byToOb(pickelFileGP)
    #     No need to update the file with H and F
    alpha, y = group.random(), group.random()
    egga = gp['egg'] ** alpha
    gy = gp['g1'] ** y
    pk = {'name': authName, 'egga': egga, 'gy': gy}
    sk = {'name': authName, 'alpha': alpha, 'y': y}
    print("Authsetup: %s" % authName)
    print(pk)
    print(sk)
    return pk, sk



if __name__ == '__main__':
    #pdb.set_trace()
    gpWithoutHF = setup()
    byteGPWithoutHF = obToBy(gpWithoutHF)
    fileName = "GlobalParameters.pkl"
    pickleDump(byteGPWithoutHF, fileName)

    readFileGP = readFile('examplePickle')
    authName = 'Redwan'
    pk, sk = authSetup(readFileGP, authName)
    bytePK = obToBy(pk)
    byteSK = obToBy(sk)
    fileNamePK = 'PK' + '@' + authName + '.pkl'
    fileNameSK = 'SK' + '@' + authName + '.pkl'
    pickleDump(bytePK, fileNamePK)
    pickleDump(byteSK, fileNameSK)
