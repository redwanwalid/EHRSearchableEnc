import os														#yes
import pdb

#pdb.set_trace()

os.system("cpabe-setup")

#cpabe-keygen
keygen = "cpabe-keygen -o sara_priv_key pub_key master_key Ortho Senior_Doctor"
os.system(keygen)
#print(keygen)

#cpabe-encrypt
encomm = "cpabe-enc pub_key " + "extensionfile.txt" + " 'Senior_Doctor or Ortho'"
#encomm = "cpabe-enc pub_key " + "extensionfile.txt" + "\n  'Senior_Doctor or Ortho' ^D"   #Not Needed
os.system(encomm)
#print(encomm)

#cpabe-decrypt
decomm = "cpabe-dec pub_key sara_priv_key " + 'extensionfile.txt' + '.cpabe'
os.system(decomm)
print(decomm)