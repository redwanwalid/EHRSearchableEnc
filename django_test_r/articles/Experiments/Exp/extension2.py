from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.bsw07 import BSW07
from charm.core.engine.util import objectToBytes, bytesToObject
import pdb
import pickle

def main():
    # instantiate a bilinear pairing map
    # 'MNT224' represents an asymmetric curve with 224-bit base field

    pairing_group = PairingGroup('MNT224')

    # CP-ABE under DLIN (2-linear)
    cpabe = BSW07(pairing_group, 2)

    # run the set up
    (pk, msk) = cpabe.setup()
    #print(type(pk))
    #print(type(msk))

    # generate a Patient key
    patient_attr_list = ['PATIENT', 'SMART-1032702']
    #print(type(patient_attr_list))
    patient_key = cpabe.keygen(pk, msk, patient_attr_list)

    # generate a Practitioiner key
    practitioner_attr_list = ['PRACTITIONER', 'SMART-PRACTITIONER-72004454']
    practitioner_key = cpabe.keygen(pk, msk, practitioner_attr_list)

    # generate a Practitioiner#2 key
    practitioner2_attr_list = ['PRACTITIONER', 'SMART-PRACTITIONER-90000001']
    practitioner2_key = cpabe.keygen(pk, msk, practitioner2_attr_list)

    # choose a random message pretend to be patient's record
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/examplePickle'
    #f = open(filepath, 'r')
    #filecontents = f.read()
    #print(filecontents)
    #a = objectToBytes(filecontents, pairing_group)
    #msg = pairing_group.deserialize(a)

    msg = pairing_group.random(GT)
    #print('Message', msg)
    #print('Type of Message', type(msg))
    #msg = 'Redwan

    # generate a ciphertext
    policy_str = '((PATIENT and SMART-1032702) or (PRACTITIONER and SMART-PRACTITIONER-72004454))'
    #print(type(policy_str))
    #pdb.set_trace()
    ctxt = cpabe.encrypt(pk, msg, policy_str)
    #print(ctxt)

    # decryption as Patientn
    #pdb.set_trace()
    rec_msg = cpabe.decrypt(pk, ctxt, patient_key)
    if rec_msg == msg:
        print("Successful decryption as a Patient.")
        #print(rec_msg)
    else:
        print("Decryption as a Patient failed.")

    # decryption as Practitioner
    rec_msg = cpabe.decrypt(pk, ctxt, practitioner_key)
    if rec_msg == msg:
        print("Successful decryption as a Practitioner.")
        #print(rec_msg)
    else:
        print("Decryption as a Practitioner failed.")

    # decryption as Practitioner#2
    rec_msg = cpabe.decrypt(pk, ctxt, practitioner2_key)
    if rec_msg == msg:
        print("Successful decryption as a Practitioner#2.")
        #print(rec_msg)
    else:
        print("Decryption as a Practitioner#2 failed.")


if __name__ == "__main__":
    main()