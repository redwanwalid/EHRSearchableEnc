import hashlib
import pdb
import pickle

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)


# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())

# hash_object = hashlib.md5(b'Redwan')
# print(hash_object.hexdigest())

mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())
UserToken = hash_object.hexdigest()
# print(UserToken)

def CreateToken(request):
    # uid = request.GET.get('uid', '')
    query = request.GET.get()
    hash_object = hashlib.md5(query.encode())
    UserToken = hash_object.hexdigest()

    return UserToken

Word_Token = []
Inter_List = []
Next_List = []
Final_list = []
Hashes = []
Indexes = []
QueryResult = []

'''
with open('Prescription.html') as f:
    content = f.read()
    f.close()


# print(content)

x = content.split(" ")
# print(x)
# print(type(x))


for word in x:
    Word_Token.append(word.lower())
    # print(word)
    # print(type(word))

# print(Word_Token)

for word in Word_Token:
    Inter_List.append(word.replace(".", ""))
    # a_string = word.replace(".", "")

# print(Inter_List)

for word in Inter_List:
    # print(word)
    Next_List.append(word.replace("\n", ""))

# print(Next_List)

for word in Next_List:
    Final_list.append(word.replace("'s", ""))

print(Final_list)

for word in Final_list:
    hash_object = hashlib.md5(word.encode())
    a = hash_object.hexdigest()
    # print(hash_object.hexdigest())
    Hashes.append(a)

print(Hashes)

# print(type(Hashes))

# print(len(Hashes))

# A = [[] * 2] * len(Hashes)
# print(A)

i = len(Hashes)
# print(i)

# print(range(i))

# for a in range(i):
#     A[a][a] =
#     print(a)
#     for Hash in Hashes:
#         print(a)
        # A[0] = Hash
        # A[i][0] = Hash

# print(A)

file = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/SearchExp/Prescription.html'


num = len(Hashes)

for j in range(num):
    column = []
    for i in range(2):
        # print(len(column))
        column.append(file)
        # print(column)
    Indexes.append(column)

i = 0
# print(cinema)
# pdb.set_trace()
for Hash in Hashes:
    Indexes[i][0] = Hash
    i = i + 1

print(Indexes)
print(type(Indexes))
with open('index.data', 'wb') as filehandle:
    pickle.dump(Indexes, filehandle)
# print(Indexes[17][0])


# pdb.set_trace()
for ind in Indexes:
    for i in range(1):
        # print(ind[i])
        if UserToken == ind[i]:
            # print('There is a match')
            # print(ind)
            QueryResult.append(ind)
        # else:
            # print('Not a match')
    # print(ind)
    # if UserToken ==

# print(QueryResult)

'''

with open('index.data', 'rb') as filehandle:
    Indexes = pickle.load(filehandle)
    filehandle.close()

print(Indexes)

def matching(token):
    for ind in Indexes:
        for i in range(1):
            # print(ind[i])
            if UserToken == ind[i]:
                # print('There is a match')
                # print(ind)
                QueryResult.append(ind)

    return QueryResult

Result = matching(UserToken)

print(Result)

x = 0

for res in Result:
    # print(res)
    # print(res[x][1])
    for x in range(1,2):
        a = res[x]
        # print(a)
        with open(a) as g:
            filecontents = g.read()
            g.close()
    x = x + 1

print(filecontents)

