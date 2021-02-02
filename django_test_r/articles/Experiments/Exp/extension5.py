from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.toolbox.symcrypto import SymmetricCryptoAbstraction,AuthenticatedCryptoAbstraction, MessageAuthenticator
from charm.test.toolbox.symcrypto_test import SymmetricCryptoAbstractionTest
from charm.core.math.pairing import hashPair as extractor
import pdb
from charm.core.engine.util import objectToBytes, bytesToObject

# groupObj = PairingGroup('SS512')
# msg = 'Redwan'
# print(msg)
# ran = groupObj.random(GT)
# a = SymmetricCryptoAbstraction(sha2(ran))
# ct = a.encrypt(msg)
# print(ct)
# b = SymmetricCryptoAbstraction(sha2(ran))
# dmsg = b.decrypt(ct);
# print(dmsg)



from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.bsw07 import BSW07
from charm.core.engine.util import objectToBytes, bytesToObject
import pdb
import pickle


groupObj = PairingGroup('SS512')
cpabe = BSW07(groupObj, 2)
(pk, msk) = cpabe.setup()
print("PK =>", pk)
print("MSK =>", msk)

patient_attr_list = ['PATIENT', 'SMART-1032702']
patient_key = cpabe.keygen(pk, msk, patient_attr_list)

practitioner_attr_list = ['PRACTITIONER', 'SMART-PRACTITIONER-72004454']
practitioner_key = cpabe.keygen(pk, msk, practitioner_attr_list)

practitioner2_attr_list = ['PRACTITIONER', 'SMART-PRACTITIONER-90000001']
practitioner2_key = cpabe.keygen(pk, msk, practitioner2_attr_list)

filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/extensionfile.txt'
f = open(filepath, 'r')
filecontents = f.read()
print("File Contents =>", filecontents)

# Encrypting the file with AES and returning AESKey and CipherText encrypted by AES
keyAES = groupObj.random(GT)
symcrypt = AuthenticatedCryptoAbstraction(extractor(keyAES))  # or SymmetricCryptoAbstraction without authentication
ciphertext = symcrypt.encrypt(filecontents)
#print(keyAES)
print("Ciphertext =>", ciphertext)

# AESKey becomes message for the MA_ABE to encrypt
message = keyAES
print("Message =>", message)

policy_str = '((PATIENT and SMART-1032702) or (PRACTITIONER and SMART-PRACTITIONER-72004454))'
ctxt = cpabe.encrypt(pk, message, policy_str)
print("Actual Ciphertext =>",ctxt)

# Decrypting AES key from MA_ABE decryption using user secret key
rec_msg = cpabe.decrypt(pk, ctxt, patient_key)
#print(rec_msg)

rec_msg_pr1 = cpabe.decrypt(pk, ctxt, practitioner_key)

rec_msg_pr2 = cpabe.decrypt(pk, ctxt, practitioner2_key)

# Decrypting File to using AES key
# ciphertext, rec_msg
ciphertext = objectToBytes(ciphertext, groupObj)
ct = bytesToObject(ciphertext, groupObj)

symcrypt = AuthenticatedCryptoAbstraction(extractor(rec_msg))
recoveredMsg = symcrypt.decrypt(ct)
print("Decrypted File using AES:")
print(recoveredMsg.decode("utf-8"))

# def main():
#     #pdb.set_trace()
#     #
#     # def testAESCBC(self):
#     #     self.MsgtestAESCBC(b"hello world")
#
#
#     def testAESCBCLong(self):
#         self.MsgtestAESCBC(b"Lots of people working in cryptography have no deep \
#        concern with real application issues. They are trying to discover things \
#         clever enough to write papers about -- Whitfield Diffie.")
#
#
#     def testAESCBC_Seperate(self):
#         self.MsgTestAESCBCSeperate(b"Lots of people working in cryptography have no deep \
#         concern with real application issues. They are trying to discover things \
#         clever enough to write papers about -- Whitfield Diffie.")
#
#
#     def MsgtestAESCBC(self, msg):
#         groupObj = PairingGroup('SS512')
#         a = SymmetricCryptoAbstraction(sha2(groupObj.random(GT)))
#         ct = a.encrypt(msg)
#         dmsg = a.decrypt(ct);
#         assert msg == dmsg, 'o: =>%s\nm: =>%s' % (msg, dmsg)
#
#
#     def MsgTestAESCBCSeperate(self, msg):
#         groupObj = PairingGroup('SS512')
#         ran = groupObj.random(GT)
#         a = SymmetricCryptoAbstraction(sha2(ran))
#         ct = a.encrypt(msg)
#         b = SymmetricCryptoAbstraction(sha2(ran))
#         dmsg = b.decrypt(ct);
#         assert msg == dmsg, 'o: =>%s\nm: =>%s' % (msg, dmsg)
#
#
# if __name__ == "__main__":
#     a = 'Hello'
#     msg = SymmetricCryptoAbstractionTest.testAESCBC()
#
#     MsgtestAESCBC(msg)