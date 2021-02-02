#
#
# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# print("The original list is : " + str(test_list))
#
# # using naive method
# # to remove duplicated
# # from list
# res = []
# for i in test_list:
# 	if i not in res:
# 		res.append(i)
#
# # printing list after removal
# print ("The list after removing duplicates : " + str(res))
#
#
# def search(request):
# 	query = request.GET.get('query', '')
#
# 	hash_object = hashlib.md5(query.encode())
# 	UserToken = hash_object.hexdigest()
#
# 	patientData = []
# 	patients = PatientInfo.objects.all()
#
# 	with open('EHRindexFinal.data', 'rb') as filehandle:
# 		Indexes = pickle.load(filehandle)
# 		filehandle.close()
#
# 	for p in patients:
# 		for ind in Indexes:
# 			for i in range(1):
# 				# print(ind[i])
# 				for x in range(1,2):
# 					if UserToken == ind[i] and p.patientName == ind[x]:
# 						# if p.patientName == ind[x]:
# 						# print('There is a match')
# 						print(p.patientName)
# 							# patientData.append(p)
# 						if p not in patientData:
# 							patientData.append(p)
# 							# QueryResult.append(ind)
#
# 	return render(request, 'patientselectTESTcopy.html', {'doctorName' : loggedinUsers[0], 'patientData' : patientData})

from random import shuffle, seed
from faker.providers.person.en import Provider

# first_names = list(set(Provider.first_names))
#
# seed(4321)
# shuffle(first_names)
# print(len(first_names))
#
# # print(first_names[0:1000])
# for p in first_names:
# 	print(p)

'''
a = [('Medication', 'M'), ('DoctorNotes', 'M'), ('ImmunizationDates', 'R'), ('LabResults', 'R'), ('Diagnoses', 'M'), ('Prescription', 'M')]
b = []
print(a)

for x in a:
	print(x)
	print(x[0])
	if x[0] not in b:
		b.append(x[0])

print(b)

# print(b)
'''

x = ['Redwan', 'Charlotte', 'Richard', 'George']
print(len(x))
i = 2
while(i<10):
    print(x[len(x) - i])
    i = i + 2


# print(x[-5])



