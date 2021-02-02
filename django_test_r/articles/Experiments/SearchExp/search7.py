import hashlib
import pdb
import pickle

QueryResult = []

with open('EHRindexFinal.data', 'rb') as filehandle:
    EHRIndexes = pickle.load(filehandle)
    filehandle.close()

# print(EHRIndexes)


mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())
UserToken = hash_object.hexdigest()

def matching(token):
    for ind in EHRIndexes:
        for i in range(1):
            # print(ind[i])
            if UserToken == ind[i]:
                # QueryResult.append(ind)
                # print('There is a match')
                # print(ind)immunization
                if ind not in QueryResult:
                    QueryResult.append(ind)

    return QueryResult

Result = matching(UserToken)

print(Result)