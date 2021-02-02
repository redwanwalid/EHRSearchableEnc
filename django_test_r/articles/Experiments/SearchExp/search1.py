from nltk import word_tokenize
import os

# os.system("cpabe-setup")



with open('Prescription.html') as f:
    content = f.read()
    f.close()


print(content)
# print(type(content))

x = content.split(" ")
# print(x)
# print(type(x))

for a in x:
    print(a)
    print(type(a))
    a.replace('.', '')
    a.replace('\n', '')
    a.replace("'s", '')
    S = a

print(S)
