from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
import pickle


if __name__ == "__main__":
  groupObj = PairingGroup('SS512')
  cpabe = CPabe_BSW07(groupObj)
  hyb_abe = HybridABEnc(cpabe, groupObj)
  (pk, mk) = hyb_abe.setup()
  access_policy = '((Patient and Smart) or (Doctor and Smart) or (Doctor and Day))'
  patient_attr_list = ['Patient', 'Smart']
  sk = hyb_abe.keygen(pk, mk, patient_attr_list)

  # sourcefile = open("source.dat", 'rb')
  # plaintext = sourcefile.read()
  # sourcefile.close()

  filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/Diagnoses.txt'
  f = open(filepath, 'r')
  filecontents = f.read()
  f.close()
  # plaintext = 'This is Redwan'
  # encryptedfile = open("encrypted.dat", 'wb')
  # ciphertext = hyb_abe.encrypt(pk, filecontents, access_policy)
  # print(ciphertext)
  # pickle.dump(ciphertext, encryptedfile)
  # encryptedfile.close()

  # encryptedfile = open("encrypted.dat", 'wb')
  # ciphertext = hyb_abe.encrypt(pk, filecontents, access_policy)
  # ciphertext["c1"]["C"] = groupObj.serialize(ciphertext["c1"]["C"])
  # for key in ciphertext["c1"]["Cy"]:
  #   ciphertext["c1"]["Cy"][key] = groupObj.serialize(ciphertext["c1"]["Cy"][key])
  # ciphertext["c1"]["C_tilde"] = groupObj.serialize(ciphertext["c1"]["C_tilde"])
  # for key in ciphertext["c1"]["Cyp"]:
  #   ciphertext["c1"]["Cyp"][key] = groupObj.serialize(ciphertext["c1"]["Cyp"][key])
  # pickle.dump(ciphertext, encryptedfile)
  # encryptedfile.close()

  # encryptedfile = open("encrypted.dat", 'rb')
  # ciphertext2 = pickle.load(encryptedfile)
  # ciphertext2["c1"]["C"] = groupObj.deserialize(ciphertext2["c1"]["C"])
  # for key in ciphertext2["c1"]["Cy"]:
  #   ciphertext2["c1"]["Cy"][key] = groupObj.deserialize(ciphertext2["c1"]["Cy"][key])
  # ciphertext2["c1"]["C_tilde"] = groupObj.deserialize(ciphertext2["c1"]["C_tilde"])
  # for key in ciphertext2["c1"]["Cyp"]:
  #   ciphertext2["c1"]["Cyp"][key] = groupObj.deserialize(ciphertext2["c1"]["Cyp"][key])
  # print
  # hyb_abe.decrypt(pk, sk, ciphertext2) == plaintext
  # encryptedfile.close()