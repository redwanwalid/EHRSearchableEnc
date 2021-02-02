'''
test_mmlwl16.py

:Authors:         Seung Geol Choi
:Date:            08/2020
'''

from charm.toolbox.pairinggroup import PairingGroup, GT
from mmlwl16 import MMLWL16


def main():
    # instantiate a bilinear pairing map
    pairing_group = PairingGroup('MNT224')
    
    cpabe = MMLWL16(pairing_group, 2)

    # run the set up
    (pk, msk) = cpabe.setup()

    # generate a key
    attr_list = ['ONE', 'TWO', 'THREE']
    key = cpabe.keygen(pk, msk, attr_list)

    # choose a random message
    msg = ['hello', 'world']
   
    # generate a ciphertext
    policy_str = '((ONE and THREE) and (TWO OR FOUR))'
    ctxt = cpabe.encrypt(pk, msg, policy_str)

    # generate a token
    token1 = cpabe.Token(pk, 'hello', key)
    token2 = cpabe.Token(pk, 'world', key)
    token3 = cpabe.Token(pk, 'python', key)

    # decryption
    b1 = cpabe.decrypt(pk, ctxt, token1)
    b2 = cpabe.decrypt(pk, ctxt, token2)
    b3 = cpabe.decrypt(pk, ctxt, token3)

    if debug:
        print(b1, b2, b3) 

    # generate a ciphertext
    policy_str = '((ONE and THREE) and (TWO and FOUR))'
    ctxt = cpabe.encrypt(pk, msg, policy_str)

    # generate a token
    token1 = cpabe.Token(pk, 'hello', key)
    token2 = cpabe.Token(pk, 'world', key)
    token3 = cpabe.Token(pk, 'python', key)

    # decryption
    b1 = cpabe.decrypt(pk, ctxt, token1)
    b2 = cpabe.decrypt(pk, ctxt, token2)
    b3 = cpabe.decrypt(pk, ctxt, token3)

    if debug:
        print(b1, b2, b3) 



if __name__ == "__main__":
    debug = True
    main()
