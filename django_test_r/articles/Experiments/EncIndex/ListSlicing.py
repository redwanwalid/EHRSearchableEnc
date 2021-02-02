'''
This is the logic i have applied to save remove the policy key value pair and convert to bytes and pickle dump.

'''
import pickle
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.core.engine.util import objectToBytes, bytesToObject

pairing_group = PairingGroup('MNT224')

def byToOb(bytes):
    return bytesToObject(bytes, pairing_group)


pairing_group = PairingGroup('MNT224')

# b = {'policy': 1, 'delta': [[1, 2], [3, 4]], 'E0': [1, 2], 'E1': [1, 2], 'E2': [1, 2], 'C': {'ORTHO': ([[1, 2, 3], [1, 2, 3]], [1, 2]), 'GYNAECOLOGY': ([[1, 2, 3], [1, 2, 3]], [1, 2])}}
#
# keys = ('delta', 'E0', 'E1', 'E2', 'C')
# b1 = {k: b[k] for k in keys}
# print(b1)
# print(type(b1))


# for key, value in c.items():
#     print(key, value)

'''
The exact logic used is shown below.

d = {0:1, 1:2, 2:3, 10:4, 11:5, 12:6, 100:7, 101:8, 102:9, 200:10, 201:11, 202:12}
keys = (0, 1, 2, 100, 101, 102)
d1 = {k: d[k] for k in keys}
print(d1)

'''

# This is after reading it from the pickle file
a = [{'delta': [[1, 2], [3, 4]], 'E0': [1, 2], 'E1': [1, 2], 'E2': [1, 2], 'C': {'ORTHO': ([[1, 2, 3], [1, 2, 3]], [1, 2]), 'GYNAECOLOGY': ([[1, 2, 3], [1, 2, 3]], [1, 2])}}, 'Philip']
print(a)

b = a[0]
# print(b)

# c = {'policy': (ORTHO and GYNAECOLOGY)}
c = {'policy': 11}
# e1 = {k: b[k] for k in FirstKey}
# print(c)
# c.update(b)
# print(c)

# d = c.update(b)
# print(d)

# print(a[1])
# print(type(a[1]))

# a[0] = c
# print(a[0])

# Indexes = []
# Indexes.append(a[0])
# Indexes.append(a[1])
# print(Indexes)

# with open('EHRIndexThreePatient.data', 'rb') as filehandle:
#     ByteCTXT = pickle.load(filehandle)
#     filehandle.close()
#
# ctxt = byToOb(ByteCTXT)
# print(ctxt)
# for a in ctxt:
#     print(a[0])
#     print(a[1])

# policy_str = '((Ortho) and (Gynaecology))'
#
# # c = {'policy': (ORTHO and GYNAECOLOGY)}
#
# d = self.util.createPolicy(policy_str)
# print(d)
#
# def test(self):
#     policy = self.util.createPolicy(policy_str)
#     return {'policy': policy}

from mmlwl16 import MMLWL16

pairing_group = PairingGroup('MNT224')

cpabe = MMLWL16(pairing_group, 2)


pol = cpabe.policy()
# print(pol)
# print(type(pol))

print(a[0])
pol.update(a[0])
print(pol)

ind = []
# for x in a:
#     print(x)
#     print(pol)
    #
    # for i in range(1):
    #     print(x[i])
    #     # pol.update(x[i])
    #     print(pol)
    #     # print(a)