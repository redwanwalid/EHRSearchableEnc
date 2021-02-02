from charm.toolbox.symcrypto import SymmetricCryptoAbstraction,AuthenticatedCryptoAbstraction, MessageAuthenticator
from charm.core.math.pairing import hashPair as extractor
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.bsw07 import BSW07
from charm.core.engine.util import objectToBytes, bytesToObject


groupObj = PairingGroup('SS512')
#groupObj = PairingGroup('MNT224')
cpabe = BSW07(groupObj, 2)
(pk, msk) = cpabe.setup()
#print("PK =>", pk)
#print("MSK =>", msk)

patient_attr_list = ['PATIENT', 'SMART-1032702']
patient_key = cpabe.keygen(pk, msk, patient_attr_list)

practitioner_attr_list = ['CARDIOLOGY','DOCTOR', 'DAY']
practitioner_key = cpabe.keygen(pk, msk, practitioner_attr_list)

practitioner2_attr_list = ['PRACTITIONER', 'SMART-PRACTITIONER-72004454']
practitioner2_key = cpabe.keygen(pk, msk, practitioner2_attr_list)

#extensionfile.txt is taken as an EHR for example
filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/extensionfile.txt'
f = open(filepath, 'r')
filecontents = f.read()
print("File Contents =>", filecontents)

# Encrypting the file with AES and returning AESKey and CipherText encrypted by AES
keyAES = groupObj.random(GT)
symcrypt = AuthenticatedCryptoAbstraction(extractor(keyAES))  # or SymmetricCryptoAbstraction without authentication
ciphertext = symcrypt.encrypt(filecontents)
#print(keyAES)
#print("Ciphertext =>", ciphertext)

# AESKey becomes message for the MA_ABE to encrypt
message = keyAES
#print("Message =>", message)

#policy_str = '(CARDIOLOGY and DOCTOR and DAY)'
policy_str = '((PATIENT and SMART-1032702) or (PRACTITIONER and SMART-PRACTITIONER-72004454) or (CARDIOLOGY and DOCTOR and DAY))'
# print(pk)
# print(message)
# print(policy_str)
ctxt = cpabe.encrypt(pk, message, policy_str)
#print("ABE Ciphertext =>",ctxt)

# Decrypting AES key from MA_ABE decryption using user secret key
rec_msg = cpabe.decrypt(pk, ctxt, patient_key)

rec_msg_pr1 = cpabe.decrypt(pk, ctxt, practitioner_key)

rec_msg_pr2 = cpabe.decrypt(pk, ctxt, practitioner2_key)

# Decrypting File to using AES key
# ciphertext, rec_msg
ciphertext = objectToBytes(ciphertext, groupObj)
ct = bytesToObject(ciphertext, groupObj)

symcrypt = AuthenticatedCryptoAbstraction(extractor(rec_msg_pr1))
recoveredMsg = symcrypt.decrypt(ct)
print("Decrypted File using AES:")
print(recoveredMsg.decode("utf-8"))

policy_str2 = '(CARDIOLOGY and DOCTOR and DAY)'
# print(pk)
# print(message)
# print(policy_str2)
ctxt2 = cpabe.encrypt(pk, message, policy_str2)
#print("ABE Ciphertext_2 =>",ctxt2)

rec_msg_pr12 = cpabe.decrypt(pk, ctxt2, practitioner_key)
ct2 = bytesToObject(ciphertext, groupObj)

symcrypt2 = AuthenticatedCryptoAbstraction(extractor(rec_msg_pr12))
recoveredMsg2 = symcrypt.decrypt(ct2)
print("Decrypted File using AES:")
print(recoveredMsg2.decode("utf-8"))


