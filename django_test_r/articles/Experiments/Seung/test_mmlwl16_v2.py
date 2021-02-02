'''
test_mmlwl16.py

:Authors:         Seung Geol Choi
:Date:            08/2020
'''

from charm.toolbox.pairinggroup import PairingGroup, GT
from mmlwl16 import MMLWL16
import pickle
from charm.core.engine.util import objectToBytes, bytesToObject
from charm.toolbox.symcrypto import AuthenticatedCryptoAbstraction, SymmetricCryptoAbstraction
from charm.core.math.pairing import hashPair as extractor

debug = True

# instantiate a bilinear pairing map
pairing_group = PairingGroup('MNT224')

def pickleDump(bytes, fileName):
    pickle.dump(bytes, open(fileName, 'wb'))


def pickleLoad(pickelFile):
    return pickle.load(pickelFile)


def obToBy(dic):
    return objectToBytes(dic, pairing_group)


def byToOb(bytes):
    return bytesToObject(bytes, pairing_group)


def readFile(fileName):
    readF = open(fileName, 'rb')
    return readF

def encryptAES(encryptionFileAES):
    keyAES = pairing_group.random(GT)
    symcrypt = AuthenticatedCryptoAbstraction(extractor(keyAES))  # or SymmetricCryptoAbstraction without authentication
    ciphertext = symcrypt.encrypt(encryptionFileAES)

    return keyAES, ciphertext

def decryptAES(readFileCipherText, keyAES):
    pickleFileCipherText = pickleLoad(readFileCipherText)
    ct = byToOb(pickleFileCipherText)

    symcrypt = AuthenticatedCryptoAbstraction(extractor(keyAES))
    recoveredMsg = symcrypt.decrypt(ct)
    print("Decrypted File using AES:")
    print(recoveredMsg.decode("utf-8"))
    return recoveredMsg

cpabe = MMLWL16(pairing_group, 2)

# run the set up
(pk, msk) = cpabe.setup()
bytePK = obToBy(pk)
byteMSK = obToBy(msk)
FilePK = "PK.pkl"
FileMSK = "MSK.pkl"
pickleDump(bytePK, FilePK)
pickleDump(bytePK, FileMSK)
# print('Public Key:', pk)                       #public key
# print('Master Key:', msk)                      #master key

# generate a key
attr_list = ['ONE', 'TWO', 'THREE']
key = cpabe.keygen(pk, msk, attr_list)
byteKey = obToBy(key)
FileKey = "Key.pkl"
pickleDump(byteKey, FileKey)
# print('Private Key:', key)                      #private key

# choose a random message
# msg = ['hello', 'world']
msg = 'hello'
keyAES, ciphertext = encryptAES(msg)
message = keyAES
# msg = ['hello world', 'the world is big']         #It does not work
# print('Message:', msg)

# generate a ciphertext
policy_str = '((ONE and THREE) and (TWO OR FOUR))'

ctxt = cpabe.encrypt(pk, message, policy_str)        #It was supposed to generate ctxt and index
byteCTXT = obToBy(ctxt)
FileCTXT = "CTXT.pkl"
pickleDump(byteCTXT, FileCTXT)
# print('Ciphertext', ctxt)

# generate a token
token1 = cpabe.Token(pk, 'hello', key)
# print('Token1:', token1)
token2 = cpabe.Token(pk, 'world', key)
token3 = cpabe.Token(pk, 'python', key)


# decryption
b1 = cpabe.decrypt(pk, ctxt, token1)
# print('b1:', b1)
b2 = cpabe.decrypt(pk, ctxt, token2)
b3 = cpabe.decrypt(pk, ctxt, token3)

if debug:
    print(b1, b2, b3)

# generate a ciphertext
# policy_str = '((ONE and THREE) and (TWO and FOUR))'
# ctxt = cpabe.encrypt(pk, msg, policy_str)

# generate a token
# token1 = cpabe.Token(pk, 'hello', key)
# token2 = cpabe.Token(pk, 'world', key)
# token3 = cpabe.Token(pk, 'python', key)

# decryption
# b1 = cpabe.decrypt(pk, ctxt, token1)
# b2 = cpabe.decrypt(pk, ctxt, token2)
# b3 = cpabe.decrypt(pk, ctxt, token3)

if debug:
    print(b1, b2, b3)

