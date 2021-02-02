'''
| From: "m(2)-ABKS: Attribute-based multi-keyword search over encrypted
| personal health records in multi-owner setting"
| Published in: 2016
| Available from: https://ink.library.smu.edu.sg/sis_research/3272/
| Security Assumption: Generic group model
|
| type:           ciphertext-policy searchable attribute-based encryption
| setting:        Pairing

:Authors:         Seung Geol Choi
:Date:            08/2020
'''

from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.ABEnc import ABEnc
from msp import MSP

debug = False


class MMLWL16(ABEnc):

    def __init__(self, group_obj, verbose=False):
        ABEnc.__init__(self)
        self.group = group_obj
        self.util = MSP(self.group, verbose)

    def setup(self):
        """
        Generates public key and master secret key.
        """

        if debug:
            print('Setup algorithm:\n')

        # pick a random element each from two source groups
        g1 = self.group.random(G1)
        g2 = self.group.random(G2)

        alpha = self.group.random(ZR)
        beta = self.group.random(ZR)
        gamma = self.group.random(ZR)

        X1 = g1**alpha
        X2 = g2**alpha
        Y1 = g1**beta
        Y2 = g2**beta
        Z1 = g1**gamma
        Z2 = g2**gamma  

        pk = {'g1': g1, 'g2':g2, 'X1': X1, 'X2':X2, 'Y1':Y1, 'Y2':Y2, 'Z1':Z1, 'Z2':Z2} 
        msk = {'alpha': alpha, 'beta':beta, 'gamma':gamma}
        return pk, msk

    def keygen(self, pk, msk, attr_list):
        """
        Generate a key for a set of attributes.
        """

        if debug:
            print('Key generation algorithm:\n')


        r = self.group.random(ZR)
        beta_inverse = 1 / msk['beta']
        #print("beta_inverse:", beta_inverse, msk['beta'], beta_inverse*msk['beta']) 

        pi = pk['g2'] ** ( ( msk['alpha'] * msk['gamma'] - r ) * beta_inverse ) 

        K = {}
        g_r = pk['g1'] ** r
        for attr in attr_list:
            r_attr = self.group.random(ZR)
            k_attr1 = g_r * ( self.group.hash(str(attr),G1) ** r_attr )
            k_attr2 = pk['g2'] ** r_attr
            K[attr] = (k_attr1, k_attr2)

        return {'attr_list': attr_list, 'pi': pi, 'K': K}

    def encrypt(self, pk, kws, policy_str):
        """
         Encrypt an indices for keywords kws under a policy string.
        """

        if debug:
            print('Encrypt-Index algorithm:\n')

        policy = self.util.createPolicy(policy_str)
        mono_span_prog = self.util.convert_policy_to_msp(policy)
        num_cols = self.util.len_longest_row

        # pick randomness
        u = []
        for i in range(num_cols):
            rand = self.group.random(ZR)
            u.append(rand)
        r2 = u[0]    # shared secret

        r1 = self.group.random(ZR)

        delta = []
        for kw in kws:
            di = pk['X1'] ** (r1 * self.group.hash(kw, ZR))
            delta.append(di)

        E0 = pk['X1'] ** r2
        E1 = pk['Y1'] ** r2
        E2 = pk['Z1'] ** r1

        C = {}
        for attr, row in mono_span_prog.items():
            cols = len(row)
            sum = 0
            for i in range(cols):
                sum += row[i] * u[i]
            attr_stripped = self.util.strip_index(attr)
            c_i1 = pk['g2'] ** sum
            c_i2 = self.group.hash(str(attr_stripped), G1) ** sum
            C[attr] = (c_i1, c_i2)

        return {'policy': policy, 'delta': delta, 'E0':E0, 'E1':E1, 'E2':E2, 'C': C}

    def Token(self, pk, kw, key):
        s = self.group.random(ZR)

        T1 = pk['X2'] ** (s * self.group.hash(kw, ZR))
        T2 = pk['Z2'] ** s
        T3 = key['pi'] ** s
        
        KK = {}
        for attr in key['attr_list']:
            (k_attr1, k_attr2) = key['K'][attr] 
            KK[attr] = (k_attr1**s, k_attr2**s)

        return {'attr_list': key['attr_list'], 'K': KK, 'T1': T1, 'T2':T2, 'T3':T3}


    def decrypt(self, pk, ctxt, key):
        """
         Decrypt ciphertext ctxt with key key.
        """

        if debug:
            print('Decryption algorithm:\n')

        nodes = self.util.prune(ctxt['policy'], key['attr_list'])
        if not nodes:
            print ("Policy not satisfied.")
            return False

        prod = 1
        for node in nodes:
            attr = node.getAttributeAndIndex()
            attr_stripped = self.util.strip_index(attr)
            (c_attr1, c_attr2) = ctxt['C'][attr]
            (k_attr1, k_attr2) = key['K'][attr_stripped]
            prod *= (pair(k_attr1, c_attr1) / pair(c_attr2, k_attr2))

        right = pair(ctxt['E2'], key['T1']) * pair( ctxt['E1'], key['T3']) * prod 
        for di in ctxt['delta']:
            if pair(di * ctxt['E0'], key['T2']) == right:
                return True
        return False

