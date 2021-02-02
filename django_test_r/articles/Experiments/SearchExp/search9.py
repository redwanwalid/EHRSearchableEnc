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
    Final_list = []

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
        # Final_list = []

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

        # for word in Final_list:
        #     hash_object = hashlib.md5(word.encode())
        #     a = hash_object.hexdigest()
        #     # print(hash_object.hexdigest())
        #     Hashes.append(a)

        # print(Hashes)

    # num = len(Hashes)
    # print(num)

    for word in Final_list:
        column= []
        for i in range(1):
            # print(len(column))
            column.append(word)
            for x in range(1,2):
                column.append(patient)
            # print(column)
        Indexes.append(column)

# print(Final_list)
print(Indexes)
# print(Hashes)

# with open('EHRindexFinal.data', 'wb') as filehandle:
#     pickle.dump(Indexes, filehandle)
#     filehandle.close()


