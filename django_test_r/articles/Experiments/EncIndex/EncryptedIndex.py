'''
This is python file i have used to creare the encrypted indexes
for the searchable encyption. I have also used to pickle dump all files.

'''

import pdb
import pickle
from mmlwl16 import MMLWL16
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.core.engine.util import objectToBytes, bytesToObject

pairing_group = PairingGroup('MNT224')

cpabe = MMLWL16(pairing_group, 2)

# run the set up
(pk, msk) = cpabe.setup()

bytePK = objectToBytes(pk, pairing_group)
byteMSK = objectToBytes(msk, pairing_group)

with open('PK.data', 'wb') as filehandle:
    pickle.dump(bytePK, filehandle)
    filehandle.close()

with open('MSK.data', 'wb') as filehandle:
    pickle.dump(byteMSK, filehandle)
    filehandle.close()

# generate a key
# attr_list = ['Senior_Doctor', 'TWO', 'THREE']
attr_list = ['ORTHO', 'GYNAECOLOGY', 'BILLING']  # Attribute list should be in Block Letters
key = cpabe.keygen(pk, msk, attr_list)

byteKey = objectToBytes(key, pairing_group)

with open('Key.data', 'wb') as filehandle:
    pickle.dump(byteKey, filehandle)
    filehandle.close()

# Word_Token = []
# Inter_List = []
# Next_List = []
# Final_list = []
# Hashes = []
Indexes = []

# currentPatient = ['Andrew', 'Anne', 'Charles', 'Charlotte', 'Diana', 'Ebony', 'George', 'Harry', 'Lalita', 'Margaret', 'Martha', 'Mike', 'Peter', 'Philip']
currentPatient = ['Mike', 'Peter', 'Philip']

for patient in currentPatient:

    LabResults = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/LabResults.html'
    Prescription = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/Prescription.html'
    Medication = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/Medication.html'
    Allergies = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/Allergies.html'
    DoctorNotes = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/DoctorNotes.html'
    Diagnoses = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/Diagnoses.html'
    ImmunizationDates = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/ImmunizationDates.html'
    BillingInfo = '/Users/redwanwalid/Desktop/redwan/PatientEHRs/' + patient + '/BillingInfo.html'

    # Creating a list of filenames
    filenames = [LabResults, Prescription, Medication, Allergies, DoctorNotes, Diagnoses, ImmunizationDates, BillingInfo]

    Hashes = []
    # Final_list = []

    # pdb.set_trace()
    for file in filenames:
        Word_Token1 = []
        Word_Token2 = []
        Word_Token3 = []
        Word_Token4 = []
        Word_Token5 = []
        Word_Token6 = []
        Word_Token7 = []
        Word_Token8 = []
        Word_Token9 = []
        Word_Token10 = []
        Word_Token11 = []
        Word_Token12 = []
        Word_Token13 = []
        Final_list = []

        # print(file)
        # print(type(file))
        with open(file) as f:
            content = f.read()
            f.close()

        x = content.split(" ")

        for word in x:
            Word_Token1.append(word.lower())

        for word in Word_Token1:
            Word_Token2.append(word.replace(".", " "))

        for word in Word_Token2:
            Word_Token3.append(word.replace("\n", ""))

        for word in Word_Token3:
            Word_Token4.append(word.replace("<li>", ""))

        for word in Word_Token4:
            Word_Token5.append(word.replace("</li>", ""))

        for word in Word_Token5:
            Word_Token6.append(word.replace("<p>", ""))

        for word in Word_Token6:
            Word_Token7.append(word.replace("</p>", ""))

        for word in Word_Token7:
            Word_Token8.append(word.replace("\t", ""))

        for word in Word_Token8:
            Word_Token9.append(word.replace(":", ""))

        for word in Word_Token9:
            Word_Token10.append(word.replace("(", ""))

        for word in Word_Token10:
            Word_Token11.append(word.replace(")", ""))

        for word in Word_Token11:
            Word_Token12.append(word.replace('"', ""))

        for word in Word_Token12:
            Final_list.append(word.replace("'s", ""))

        for word in Final_list:
            policy_str = '((Ortho) and (Gynaecology))'
            ctxt = cpabe.encrypt(pk, word, policy_str)
            keys = ('delta', 'E0', 'E1', 'E2', 'C')
            sliced = {k: ctxt[k] for k in keys}
            Hashes.append(sliced)

        # print(Hashes)

    # num = len(Hashes)
    # print(num)

    for hash in Hashes:
        column= []
        for i in range(1):
            # print(len(column))
            column.append(hash)
            for x in range(1,2):
                column.append(patient)
            # print(column)
        Indexes.append(column)

# print(Final_list)
print(Indexes)
# print(len(Indexes))
# print(type(Indexes))
# print(Indexes[1:]['policy'])
# print(type(Indexes[0][0]))

# for ind in Indexes:
#     print(ind)
#     for i in range(1):
#         print(ind[i])
#         print(type(ind[i]))
#         print('Policy:', ind[i]['policy'])
#         print(type(ind[i]['policy']))
#         print('delta:', ind[i]['delta'])
#         print(type(ind[i]['delta']))
#         print('E0:', ind[i]['E0'])
#         print(type(ind[i]['E0']))
#         print('E1:', ind[i]['E1'])
#         print(type(ind[i]['E1']))
#         print('E2:', ind[i]['E2'])
#         print(type(ind[i]['E2']))
#         print('C:', ind[i]['C'])
#         print(type(ind[i]['C']))
#         for x in range(1, 2):
#             print(ind[x])

byteIndexes = objectToBytes(Indexes, pairing_group)
# print(byteIndexes)
# print(Hashes)

with open('EHRindexThreePatient.data', 'wb') as filehandle:
    pickle.dump(byteIndexes, filehandle)
    filehandle.close()

# with open('EHRIndexFinal.data', 'rb') as filehandle:
#     ByteCTXT = pickle.load(filehandle)
#     filehandle.close()

# ctxt = byToOb(ByteCTXT)
# print(ctxt)