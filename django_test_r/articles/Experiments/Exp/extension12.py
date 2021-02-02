import os
import pdb

# os.system("cpabe-setup")

# patient_attr_list = 'PATIENT', 'SMART']
# patient_sec_key = "cpabe-keygen -o patient_key pub_key master_key PATIENT SMART"
# os.system(patient_sec_key)

# filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/Diagnoses.txt'
# encomm = "cpabe-enc pub_key " + filepath + " 'PATIENT or SMART'"
# os.system(encomm)

# decomm = "cpabe-dec pub_key patient_key " + filepath + '.cpabe'
# os.system(decomm)






# encomm = "cpabe-enc pub_key " + filepath + " 'Senior_Doctor or Ortho'"
# 		os.system(encomm)

# cpabe-keygen -o patient_key pub_key master_key PATIENT SMART
# cpabe-enc pub_key test.txt 'PATIENT or SMART'
# cpabe-dec pub_key patient_key test.txt.cpabe
# filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/articles/Exp/Diagnoses.txt'
# f = open(filepath, 'r')
# filecontents = f.read()


a = [('Prescription', 'M'), ('LabResults', 'R'), ('DoctorNotes', 'M'), ('Medication', 'M'), ('Diagnoses', 'M'), ('ImmunizationDates', 'R')]

# print(a[0][0])
# print(a[1][0])
# print(type(a))

# filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/a[b].html'

# pdb.set_trace()

# for x in a:
#     # print(x)
#     b = 0
#     print(x[b])
#
#     S = x[b]
#
#     filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/Harry' + '/' + S + '.html'
#     print(filepath)
# cpabe-keygen -o priv_key pub_key master_key Senior_Doctor Ortho Gynaecology Billing
# cpabe-enc pub_key /Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/Harry/BillingInfo.html 'Senior_Doctor or Ortho or Gynaecology or Billing'

patientEHRfields = ['Diagnoses', 'Medication', 'Prescription', 'Allergies', 'LabResults', 'ImmunizationDates', 'DoctorNotes', 'BillingInfo']

# for a in patientEHRfields:
#     print(a)

for a in patientEHRfields:
    filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + 'Harry' + '/' + a + '.html'
    print(filepath)