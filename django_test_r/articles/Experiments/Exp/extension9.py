from charm.toolbox.symcrypto import SymmetricCryptoAbstraction,AuthenticatedCryptoAbstraction, MessageAuthenticator
from charm.core.math.pairing import hashPair as extractor
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.bsw07 import BSW07
from charm.core.engine.util import objectToBytes, bytesToObject
import pickle
import pdb
import json


groupObj = PairingGroup('SS512')
# groupObj = PairingGroup('MNT224')
cpabe = BSW07(groupObj, 2)
(pk, msk) = cpabe.setup()

policy_str = '((PATIENT and SMART-1032702) or (PRACTITIONER and SMART-PRACTITIONER-72004454) or (CARDIOLOGY and DOCTOR and DAY))'

keyAES = groupObj.random(GT)
message = keyAES

ctxtABE = cpabe.encrypt(pk, message, policy_str)
# filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/test.txt'
# f = open(filepath, 'a+')
# f.write(ctxtABE)
# f.close()
# tron = json.load(ctxtABE)

# with open('test.pickle', 'wb') as f:
#     print(ctxtABE, file=f)

# print(type(ctxtABE))

# print(ctxtABE)
# print(type(ctxtABE))

# byteCTXT = objectToBytes(ctxtABE, groupObj)
# pickle_out = open("ctxtABE.pickle", "wb")
# pickle.dump(ctxtABE, pickle_out)
# pickle_out.close()
#print(ctxtABE)
#pdb.set_trace()
#bytectxtABE = objectToBytes(ctxtABE, groupObj)
#a = bytesToObject(ctxtABE, groupObj)
