import hashlib
import pdb
import pickle


Word_Token = []
Inter_List = []
Next_List = []
Final_list = []
Hashes = []
Indexes = []
QueryResult = []


# mystring = input('Enter String to hash: ')
# Assumes the default UTF-8
# hash_object = hashlib.md5(mystring.encode())
# UserToken = hash_object.hexdigest()
# print(UserToken)

with open('Prescription.html') as f:
    content = f.read()
    f.close()

x = content.split(" ")

for word in x:
    Word_Token.append(word.lower())

for word in Word_Token:
    Inter_List.append(word.replace(".", ""))

for word in Inter_List:
    Next_List.append(word.replace("\n", ""))

for word in Next_List:
    Final_list.append(word.replace("'s", ""))

for word in Final_list:
    hash_object = hashlib.md5(word.encode())
    a = hash_object.hexdigest()
    # print(hash_object.hexdigest())
    Hashes.append(a)

# print(Hashes)

file = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/SearchExp/Prescription.html'


num = len(Hashes)
# print(num)

for j in range(num):
    column = []
    for i in range(2):
        # print(len(column))
        column.append(file)
        # print(column)
    Indexes.append(column)

# print(Indexes)

i = 0
# print(cinema)
# pdb.set_trace()
for Hash in Hashes:
    Indexes[i][0] = Hash
    i = i + 1




















# print(Indexes)

# for i in range(1):
    # print(i)
    # for x in range(1,2):
    #     print(x)