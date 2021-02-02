import hashlib
import pdb
import pickle

# Word_Token = []
# Inter_List = []
# Next_List = []
# Final_list = []
Hashes = []
Indexes = []

currentPatient = input('Enter Patient Name: ')

LabResults = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/LabResults.html'
Prescription = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/Prescription.html'
Medication = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/Medication.html'
Allergies = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/Allergies.html'
DoctorNotes = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/DoctorNotes.html'
Diagnoses = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/Diagnoses.html'
ImmunizationDates = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/ImmunizationDates.html'
BillingInfo = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + currentPatient + '/BillingInfo.html'

# Creating a list of filenames
filenames = [LabResults, Prescription, Medication, Allergies, DoctorNotes, Diagnoses, ImmunizationDates, BillingInfo]

# pdb.set_trace()
for file in filenames:
    Word_Token = []
    Inter_List = []
    Next_List = []
    Final_list = []
    # print(file)
    # print(type(file))
    with open(file) as f:
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

# print(Final_list)
print(Hashes)

num = len(Hashes)
print(num)

for hash in Hashes:
    column= []
    for i in range(1):
        # print(len(column))
        column.append(hash)
        for x in range(1,2):
            column.append(currentPatient)
        # print(column)
    Indexes.append(column)

print(Indexes)
