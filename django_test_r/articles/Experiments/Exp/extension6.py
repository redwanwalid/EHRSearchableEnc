from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.toolbox.symcrypto import SymmetricCryptoAbstraction,AuthenticatedCryptoAbstraction, MessageAuthenticator
from charm.test.toolbox.symcrypto_test import SymmetricCryptoAbstractionTest
from charm.core.math.pairing import hashPair as extractor
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.bsw07 import BSW07
from charm.core.engine.util import objectToBytes, bytesToObject
import pdb


# @Output(pk_t, mk_t)
def setup(self, SecurityParameter):  # Nothing to change in this function
    g, gp = group.random(G1), group.random(G2)
    alpha, beta = group.random(ZR), group.random(ZR)
    # initialize pre-processing for generators
    g.initPP();
    gp.initPP()

    h = g ** beta;
    f = g ** ~beta
    e_gg_alpha = pair(g, gp ** alpha)

    pk = {'g': g, 'g2': gp, 'h': h, 'f': f, 'e_gg_alpha': e_gg_alpha}
    mk = {'beta': beta, 'g2_alpha': gp ** alpha}
    tsk = {}
    return (pk, mk)











def main():
    #pdb.set_trace()
    groupObj = PairingGroup('SS512')

    # cpabe = CPabe_BSW07(groupObj)














if __name__ == "__main__":
    debug = True
    #pdb.set_trace()
    main()
