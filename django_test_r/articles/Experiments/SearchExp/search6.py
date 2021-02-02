import hashlib
import pdb
import pickle

# Word_Token = []
# Inter_List = []
# Next_List = []
# Final_list = []
# Hashes = []
Indexes = []

currentPatient = ['Andrew', 'Anne', 'Charles', 'Charlotte', 'Diana', 'Ebony', 'George', 'Harry', 'Lalita', 'Margaret', 'Martha', 'Mike', 'Peter', 'Philip']

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

print(Indexes)

# with open('EHRindex.data', 'wb') as filehandle:
#     pickle.dump(Indexes, filehandle)
#     filehandle.close()

# with open('EHRindex.data', 'rb') as filehandle:
#     EHRIndexes = pickle.load(filehandle)
#     filehandle.close()

# print(EHRIndexes)


