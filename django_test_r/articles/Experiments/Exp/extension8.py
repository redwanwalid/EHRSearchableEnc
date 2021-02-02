from charm.toolbox.symcrypto import SymmetricCryptoAbstraction, AuthenticatedCryptoAbstraction, MessageAuthenticator
from charm.core.math.pairing import hashPair as extractor
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.bsw07 import BSW07
from charm.core.engine.util import objectToBytes, bytesToObject
import pickle
import yaml
import pdb
import ast
import json

groupObj = PairingGroup('SS512')
# groupObj = PairingGroup('MNT224')
cpabe = BSW07(groupObj, 2)
(pk, msk) = cpabe.setup()
# print("PK =>", pk)
# print("MSK =>", msk)

# Dumping PK into a pickle file
# bytePK = objectToBytes(pk, groupObj)
# print("bytePK =>", bytePK)
# pickle_out_pk = open("pk.pkl", "wb")
# pickle.dump(bytePK, pickle_out_pk)
# pickle_out_pk.close()

# Dumping MSK into a pickle file
# byteMSK = objectToBytes(msk, groupObj)
# print("byteMSK =>", byteMSK)
# pickle_out_msk = open("msk.pkl", "wb")
# pickle.dump(byteMSK, pickle_out_msk)
# pickle_out_msk.close()
# print("PK =>", pk)
# print("MSK =>", msk)

pickle_in_pk = open("pk.pkl", "rb")
# pk = pickle_in_pk.read()
# print(pk)
bytePK = pickle.load(pickle_in_pk)
pk = bytesToObject(bytePK, groupObj)
# print(bytePK)
# print("PK =>",pk)

pickle_in_msk = open("msk.pkl", "rb")
# msk = pickle_in_msk.read()
byteMSK = pickle.load(pickle_in_msk)
msk = bytesToObject(byteMSK, groupObj)
# print("BYTE MSK =>", byteMSK)
# print("MSK =>", msk)

# patient_attr_list = ['PATIENT', 'SMART']
# patient_key = cpabe.keygen(pk, msk, patient_attr_list)
# bytepatient_key = objectToBytes(patient_key, groupObj)
# pickle_out_patient_key = open("patient_key.pkl", "wb")
# pickle.dump(bytepatient_key, pickle_out_patient_key)
# pickle_out_patient_key.close()
pickle_in_patient_key = open("patient_key.pkl", "rb")
bytePatKey = pickle.load(pickle_in_patient_key)
patient_key = bytesToObject(bytePatKey, groupObj)

# practitioner_attr_list = ['CARDIOLOGY','DOCTOR', 'DAY']
# practitioner_key = cpabe.keygen(pk, msk, practitioner_attr_list)
# bytepractitioner_key = objectToBytes(practitioner_key, groupObj)
# pickle_out_practitioner_key = open("practitioner_key.pkl", "wb")
# pickle.dump(bytepractitioner_key, pickle_out_practitioner_key)
# pickle_out_practitioner_key.close()
pickle_in_practitioner_key = open("practitioner_key.pkl", "rb")
bytePracKey = pickle.load(pickle_in_practitioner_key)
practitioner_key = bytesToObject(bytePracKey, groupObj)

# practitioner2_attr_list = ['PRACTITIONER', 'SMART']
# practitioner2_key = cpabe.keygen(pk, msk, practitioner2_attr_list)
# bytepractitioner2_key = objectToBytes(practitioner2_key, groupObj)
# pickle_out_practitioner2_key = open("practitioner2_key.pkl", "wb")
# pickle.dump(bytepractitioner2_key, pickle_out_practitioner2_key)
# pickle_out_practitioner2_key.close()
pickle_in_practitioner2_key = open("practitioner2_key.pkl", "rb")
bytePracKey2 = pickle.load(pickle_in_practitioner2_key)
practitioner2_key = bytesToObject(bytePracKey2, groupObj)

# EHR for example
filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/Diagnoses.txt'
f = open(filepath, 'r')
filecontents = f.read()
# print("File Contents =>", filecontents)

# Encrypting the file with AES and returning AESKey and CipherText encrypted by AES
keyAES = groupObj.random(GT)
symcrypt = AuthenticatedCryptoAbstraction(extractor(keyAES))  # or SymmetricCryptoAbstraction without authentication
ciphertextAES = symcrypt.encrypt(filecontents)
# print(type(ciphertextAES))
byteciphertextAES = objectToBytes(ciphertextAES, groupObj)
pickle_out_ciphertextAES = open("ciphertextAES.pkl", "wb")
pickle.dump(byteciphertextAES, pickle_out_ciphertextAES)
pickle_out_ciphertextAES.close()
# print(keyAES)
# print("Ciphertext =>", ciphertext)

# AESKey becomes message for the MA_ABE to encrypt
message = keyAES
# print("Message =>", message)

# policy_str = 'DOCTOR'
policy_str = '((PATIENT and SMART) or (PRACTITIONER and SMART) or (CARDIOLOGY and DOCTOR))'
# print(pk)
# print(message)
# print(policy_str)
ctxtABE = cpabe.encrypt(pk, message, policy_str)
bytectxtABE = objectToBytes(ctxtABE, groupObj)
pickle_out_ctxtABE = open("ctxtABE.pkl", "wb")
pickle.dump(ctxtABE, pickle_out_ctxtABE)
pickle_out_ctxtABE.close()
# print(type(ctxtABE))
# with open("data_file.json", "wb") as F:
#     json.dump(ctxtABE, F, encode = "utf8")


# Special Note: Unable to dump pickle so didn't convert to Bytes, so bytestoObjects not needed
# with open('ctxtABE.pkl', 'w') as f:
#     print(ctxtABE, file=f)
#
# with open('ctxtABE.pkl', 'r') as f:
#     ctxt = f.read()
# print(ctxt)
#
#
# ctxtS = json.loads(ctxt)
# arr = bytes(ctxt, 'utf-8')
# print(arr)
# print(type(arr))
# res = json.loads(ctxt)

#     ctxt = '"' + ctxt + '"'
# print(ctxt)
# print(type(ctxt))
# ctxt = yaml.load(ctxt)
# print(ctxt)
# print(type(ctxt))
# ast.literal_eval(ctxt)
# json.loads(ctxt)
# print(type(ctxtABE))
# pdb.set_trace()



# print("ABE Ciphertext =>",ctxt)


# pickle_out_ciphertextABE = open("ctxtABE.pickle", "rb")
# byteCtxtABE = pickle.load(pickle_out_ciphertextABE)
# ctxtmsg = bytesToObject(byteCtxtABE, groupObj)


# Decrypting AES key from MA_ABE decryption using user secret key
# rec_msg = cpabe.decrypt(pk, ctxt, patient_key)

# rec_msg_pr1 = cpabe.decrypt(pk, ctxtmsg, practitioner_key)

# rec_msg_pr2 = cpabe.decrypt(pk, ctxt, practitioner2_key)

# Decrypting File to using AES key
# ciphertext, rec_msg
# ciphertext = objectToBytes(ciphertext, groupObj)
# ct = bytesToObject(ciphertext, groupObj)

# symcrypt = AuthenticatedCryptoAbstraction(extractor(rec_msg_pr1))
# recoveredMsg = symcrypt.decrypt(ct)
# print("Decrypted File using AES:")
# print(recoveredMsg.decode("utf-8"))

# policy_str2 = '(CARDIOLOGY and DOCTOR and DAY)'
# print(pk)
# print(message)
# print(policy_str2)
# ctxt2 = cpabe.encrypt(pk, message, policy_str2)
#print("ABE Ciphertext_2 =>",ctxt2)

# rec_msg_pr12 = cpabe.decrypt(pk, ctxt2, practitioner_key)
# ct2 = bytesToObject(ciphertext, groupObj)

# symcrypt2 = AuthenticatedCryptoAbstraction(extractor(rec_msg_pr12))
# recoveredMsg2 = symcrypt.decrypt(ct2)
# print("Decrypted File using AES:")
# print(recoveredMsg2.decode("utf-8"))


