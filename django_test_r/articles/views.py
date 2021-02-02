# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template 				#yes
from django.template import Context
#from django.shortcuts import render_to_response				#no
from django.shortcuts import render								#yes
from django.views.decorators.csrf import csrf_protect 			#yes
import rdflib
from rdflib import Graph, URIRef								#yes
import os														#yes
from articles.models import StaffInfo							#yes
from articles.models import PatientInfo							#yes
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
import hashlib
import pickle
from mmlwl16 import MMLWL16
from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.core.engine.util import objectToBytes, bytesToObject
import time



#export DJANGO_SETTINGS_MODULE=mysite.settings

searchtoken = []
loggedinUsers = []
# fieldsWithPermissions = []
# allowedFiles = []
Allowed_Fields = []
attributes = []
# os.system("cpabe-setup")

def hello(request):
    # name = "Maithilee"
    # html = "<html><body>Hi %s, this seems to have worked!</body></html>" %name
    # return HttpResponse(html)
    return render(request, 'home.html')


def hello_template(request):
    fname = "Maithilee"
    lname = "Joshi"
    t = get_template('hello.html')
    html = t.render({'fname' : fname, 'lname':lname})
    return HttpResponse(html)

# Simpler method for the above method
def hello_template_simple(request):
    fname = "Maithilee"
    lname = "Joshi"
    return render(request, 'hello.html', {'fname':fname, 'lname':lname})

def home(request):
    # print(patientName)
    print(loggedinUsers)
    # print(type(loggedinUsers))
    # currentPatient = loggedinUsers[1]
    # print(a)
    # currentPatient = loggedinUsers
    # print(currentPatient)
    # CurrentPat = currentPatient[1]
    # currentPatient = loggedinUsers[0]

    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]

    patientEHRfields = ['Diagnoses', 'Medication', 'Prescription', 'Allergies', 'LabResults', 'ImmunizationDates', 'DoctorNotes', 'BillingInfo']

    for a in patientEHRfields:
        #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/' + a + '.html'
        filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/' + a + '.html'
        # print(filepath)
        encomm = "cpabe-enc pub_key " + filepath + " 'Senior_Doctor or Ortho or Gynaecology or Billing'"
        os.system(encomm)
    return render(request, 'home.html')

def staffsignup(request):
    return render(request, 'staffsignup.html')

def stafflogin(request):
    return render(request, 'stafflogin.html')

#This function is saving new staff info in the database, need to check if the ontology is populating?
def staffsignup_view(request):
    uid = request.GET.get('uid', '')
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    role = request.GET.get('role', '')
    certification = request.GET.get('certification', '')
    specialization = request.GET.get('specialization', '')
    hward = request.GET.get('hward', '')

    staffData = StaffInfo.objects.all()

    for sD in staffData:
        if sD.uid == uid:
            html = "<html><body> User aready exists..! <p> Your username is %s, please go back and login using your credentials. </p> </body> </html>" %sD.username
            return HttpResponse(html)

    newUser = StaffInfo(uid = uid, username = username, password = password, role = role, certification = certification, specialization = specialization, hward = hward)
    newUser.save()
    return render(request, 'stafflogin.html')

def stafflogin_view(request):
    uid = request.GET.get('uid', '')
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')

    staffData = StaffInfo.objects.all()

    for sD in staffData:
        if ((sD.uid == uid) and (sD.username == username) and (sD.password == password)):

            #Update global array of logged in Users (Staff)
            loggedinUsers.append(username)
            print(username)
            print(loggedinUsers)
            a = loggedinUsers[0]
            print(a)

            #Get user's attributes
            uAttr = [sD.role, sD.specialization, sD.certification, sD.hward]
            attributes.extend(uAttr)
            #print(attributes)

            # If login creds are correct, then filter patients of the same ward
            patientData = []
            patients = PatientInfo.objects.all()
            # print(patients)

            for p in patients:
                # print (p.patientHward, sD.hward)
                if (p.patientHward == sD.hward):
                    # print ("here")
                    patientData.append(p)

                #Should add searchability here

            # print(patientData.patientName)

            return render(request, 'patientselectTEST.html', {'doctorName' : username, 'patientData' : patientData})

    html = "<html><body> Invalid login credentials provided..! <p> Please go back and try login using your credentials or create a new account by signing up.</p> </body> </html>"
    return HttpResponse(html)

def byToOb(bytes):
    pairing_group = PairingGroup('MNT224')
    return bytesToObject(bytes, pairing_group)

def search(request):
    query = request.GET.get('query', '')

    start_time = time.perf_counter()

    pairing_group = PairingGroup('MNT224')

    cpabe = MMLWL16(pairing_group, 2)

    patientData = []
    patients = PatientInfo.objects.all()

    with open('PK.data', 'rb') as filehandle:
        BytePK = pickle.load(filehandle)
        filehandle.close()

    pk = byToOb(BytePK)

    with open('Key.data', 'rb') as filehandle:
        ByteKey = pickle.load(filehandle)
        filehandle.close()

    key = byToOb(ByteKey)

    token1 = cpabe.Token(pk, query, key)

    print(time.perf_counter() - start_time, "seconds")

    with open('EHRindexThreePatient.data', 'rb') as filehandle:
        ByteCTXT = pickle.load(filehandle)
        filehandle.close()

    Indexes = byToOb(ByteCTXT)
    # b = ctxt[0]
    # c = {'policy': (ORTHO and GYNAECOLOGY)}
    # c.update(b)

    # ctxt[0] = c

    # Indexes = []
    # Indexes.append(ctxt[0])
    # Indexes.append(ctxt[1])

    # policy_str = '((Ortho) and (Gynaecology))'


    for p in patients:
        for ind in Indexes:
            print(ind)
            for i in range(1):
                c = cpabe.policy()
                c.update(ind[i])
                b1 = cpabe.decrypt(pk, c, token1)
                # print(ind[i])
                for x in range(1,2):
                    if b1 == True and p.patientName == ind[x] and p not in patientData:
                        print(p)
                        patientData.append(p)

    return render(request, 'patientselectTESTcopy.html', {'doctorName' : loggedinUsers[-1], 'patientData' : patientData})

def patientsignup(request):
    return render(request, 'patientsignup.html')

def patientlogin(request):
    return render(request, 'patientlogin.html')

def patientsignup_view(request):
    patientName = request.GET.get('patientName', '')
    patientPassword = request.GET.get('patientPassword', '')
    doctorName = request.GET.get('doctorName', '')
    patientHward = request.GET.get('patientHward', '')
    purpose = request.GET.get('purpose', '')

    patientData = PatientInfo.objects.all()

    for pD in patientData:
        if pD.patientName == patientName:
            html = "<html><body> User aready exists..! <p> Your username is %s, please go back and login using your credentials. </p> </body> </html>" %pD.patientName
            return HttpResponse(html)

    newUser = PatientInfo(patientName = patientName, patientPassword = patientPassword, doctorName = doctorName, patientHward = patientHward, purpose = purpose)
    newUser.save()
    return render(request, 'patientlogin.html')


def patientlogin_view(request):
    patientName = request.GET.get('patientName', '')
    patientPassword = request.GET.get('patientPassword', '')

    print(patientName)

    patientData = PatientInfo.objects.all()

    for pD in patientData:
        if ((pD.patientName == patientName) and (pD.patientPassword == patientPassword)):
            loggedinUsers.extend(['None', patientName])
            patientEHRfields = ['Diagnoses', 'Medication', 'Prescription', 'Allergies', 'LabResults', 'ImmunizationDates', 'DoctorNotes', 'BillingInfo']
            return render(request, "patientehrview.html", {'allowedFields':patientEHRfields, 'patientName' : patientName})

    return render(request, "patientlogin.html", {'error_flag' : True})


def runSPARQL(doctorName, patientName):
    g = Graph()
    #g.parse("/Users/redwanwalid/Desktop/redwan/django_test_r/EHROntology_v2.owl")
    g.parse("/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/EHROntology_v2.owl")

    sparql = "SELECT ?predicate WHERE {<http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str(doctorName) + "> ?predicate ?object .}"

    qres = g.query(sparql)

    res = []
    for row in qres:
        # print(row[0])
        # print(type(row))
        p = row[0].split('#')[1]
        # print(p)
        if (p.startswith('can')):
            permission = str(p[3])
            if (permission == 'M'):
                field = str(p[9:])
            else:
                field = str(p[7:])

            if (field and permission):
                if field != 'VitalStats':
                    res.append((field, permission))

    return res

def getSelectedPatient(request):
    selectedPatient = request.GET.get('checks')
    loggedinUsers.append(selectedPatient)
    print(loggedinUsers)
    # currentDoctor = loggedinUsers[0]
    currentDoctor = loggedinUsers[-2]

    print(selectedPatient)
    print(currentDoctor)
    print(loggedinUsers)

    fieldsWithPermissions = []
    allowedFiles = []

    fieldsWithPermissions.extend(runSPARQL(currentDoctor, selectedPatient))
    #print (fieldsWithPermissions)

    if (fieldsWithPermissions == []):
        return HttpResponse("Access Denied!")

    else:
        # allowedFiles = []
        # print(allowedFiles)
        allowedFiles.extend(fieldsWithPermissions)
        print (allowedFiles)
        for f in allowedFiles:
            # print(f[0])
            # x = f[0]
            # print(x)
            # Allowed_Fields.extend(f)
            if f[0] not in Allowed_Fields:
                Allowed_Fields.append(f[0])
        print(Allowed_Fields)
        return render(request, "patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : selectedPatient, 'doctorName' : currentDoctor, 'role' : attributes[0], 'specialization' : attributes[1], 'certification' : attributes[2], 'hward' : attributes[3]})

@xframe_options_sameorigin
def LabResults(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/LabResults.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/LabResults.html'
    cpabefile = filepath + '.cpabe'


    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
        # print ("Exception raised")

    f = open(filepath, 'r')
    filecontents = f.read()
    #print(filecontents)
    #print(type(filecontents))


    # if os.path.isfile(filepath):
    #	print('Ready to Encrypt')
        # encom = "cpabe-enc pub_key" + filepath + " 'Senior_Doctor or Ortho'"
        # os.system(encom)

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def Prescription(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/Prescription.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/Prescription.html'
    cpabefile = filepath + '.cpabe'

    if os.path.isfile(cpabefile):
        print("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
    # print ("Exception raised")

    f = open(filepath, 'r')
    filecontents = f.read()

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def Medication(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/Medication.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/Medication.html'
    cpabefile = filepath + '.cpabe'

    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
        # print ("Exception raised")

    f = open(filepath, 'r')
    filecontents = f.read()
    #print(filecontents)

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def Allergies(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #print(currentPatient)
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/Allergies.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/Allergies.html'
    cpabefile = filepath + '.cpabe'
    #print(cpabefile)

    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
        # print ("Exception raised")

    f = open(filepath, 'r')
    filecontents = f.read()
    #print(filecontents)
    #print(type(filecontents))

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def DoctorNotes(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/DoctorNotes.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/DoctorNotes.html'
    cpabefile = filepath + '.cpabe'

    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)

    f = open(filepath, 'r')
    filecontents = f.read()

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def Diagnoses(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #print(loggedinUsers[1])
    #print(currentPatient)
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/Diagnoses.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/Diagnoses.html'
    #print(filepath)
    cpabefile = filepath + '.cpabe'
    #print(cpabefile)

    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
        # print ("Exception raised")

    f = open(filepath, 'r')
    #print(f)
    filecontents = f.read()
    #print(filecontents)

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def ImmunizationDates(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/ImmunizationDates.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/ImmunizationDates.html'
    cpabefile = filepath + '.cpabe'

    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
        # print ("Exception raised")

    f = open(filepath, 'r')
    filecontents = f.read()

    return HttpResponse(filecontents)

@xframe_options_sameorigin
def BillingInfo(request):
    # currentPatient = loggedinUsers[1]
    currentPatient = loggedinUsers[-1]
    print(currentPatient)
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/BillingInfo.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/BillingInfo.html'
    cpabefile = filepath + '.cpabe'

    if os.path.isfile(cpabefile):
        print ("FOUND")
        decomm = "cpabe-dec pub_key priv_key " + filepath + '.cpabe'
        os.system(decomm)
        # print ("Exception raised")

    f = open(filepath, 'r')
    filecontents = f.read()

    return HttpResponse(filecontents)

@csrf_exempt
@xframe_options_sameorigin
def saveEdits(request):
    print(loggedinUsers)
    currentPatient = loggedinUsers[-1]
    # currentDoctor = loggedinUsers[0]
    currentDoctor = loggedinUsers[-2]

    print(currentPatient)
    print(currentDoctor)

    print(Allowed_Fields)

    editField = request.GET.get('select')
    print(editField)
    print (str(editField))

    newEdits = request.GET.get('inputEdit')
    print(newEdits)
    print (str(newEdits))

    if (not editField):
        # print(fieldsWithPermissions)
        # print(allowedFiles)
        # print(AllowedFields)
        # print(type(allowedFiles))
        for EHR_Field in Allowed_Fields:
        # for a in allowedFiles:
            # print(a)
            # b = 0
            # print(a[b])
            # EHR_Field = a[b]
            #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/' + EHR_Field + '.html'
            filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/' + EHR_Field + '.html'
            # print(filepath)
            encomm = "cpabe-enc pub_key " + filepath + " 'Senior_Doctor or Ortho or Gynaecology or Billing'"
            os.system(encomm)

        return render(request, "home.html")
        # return redirect('home.html')

    print (allowedFiles)
    editFieldIndex = [a[0] for a in allowedFiles].index(editField)
    print (editFieldIndex)
    print (fieldsWithPermissions)
    fieldpermission = fieldsWithPermissions[editFieldIndex][1]
    print (fieldpermission)

    if fieldpermission != 'M':
        html = "<html><body> You do not have edit access"
        return HttpResponse(html)

    else:
        # os.system("cpabe-keygen -o priv_key pub_key master_key Ortho Gynaecology Billing Senior_Doctor")
        #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/' + editField + '.html'
        filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/' + currentPatient + '/' + editField + '.html'
        f = open(filepath, 'a+')
        f.write("<p>")
        f.write(newEdits)
        f.write("</p>")

        conts = f.read()
        print (conts)
        encomm = "cpabe-enc pub_key " + filepath + " 'Senior_Doctor or Ortho or Gynaecology or Billing'"
        os.system(encomm)
        return render(request, "patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : currentPatient, 'doctorName' : currentDoctor, 'role' : attributes[0], 'specialization' : attributes[1], 'certification' : attributes[2], 'hward' : attributes[3]})


@xframe_options_sameorigin
def explain(request):
    #filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/accessExplain.html'
    filepath = '/afs/umbc.edu/users/r/w/rwalid1/home/EHR_application/django_test_r/PatientEHRs/accessExplain.html'
    f = open(filepath, 'r')
    filecontents = f.read()

    return HttpResponse(filecontents)
    # return render('home.html')

    # if str(newEdits).startswith('Prescription'):
    # 	field = 'Prescription'
    # elif str(newEdits).startswith('Medication'):
    # 	print ("here")
    # 	field = 'Medication'
    # elif str(newEdits).startswith('LabResults'):
    # 	field = 'LabResults'
    # elif str(newEdits).startswith('ImmunizationDates'):
    # 	field = 'ImmunizationDates'
    # elif str(newEdits).startswith('Diagnoses'):
    # 	field = 'Diagnoses'
    # elif str(newEdits).startswith('Allergies'):
    # 	field = 'Allergies'
    # elif str(newEdits).startswith('BillingInfo'):
    # 	field = 'BillingInfo'


    # fieldIndex = allowedFiles.index(field)
    # if fieldsWithPermissions[fieldIndex][1] == 'M':
    # 	filepath = '/Users/redwanwalid/Desktop/redwan/django_test_r/django_test_r/PatientEHRs/' + currentPatient + '/' + field + '.html'
    # 	f = open(filepath, 'a+')
    # 	f.write("<p>")
    # 	f.write(newEdits)
    # 	f.write("</p>")
    # 	return render_to_response("patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : currentPatient, 'doctorName' : currentDoctor})

    # else:
    # 	html = "<html><body> TODO : Pop Up Box. For now, Sorry you do not have edit access </body><html>"
    # 	return HttpResponse(html)



    # if request.POST.get("button"):
    # 	print ("Got Diagnoses!")

    # return render_to_response("patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : currentPatient, 'doctorName' : currentDoctor})
    # return render_to_response("patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : currentPatient, 'doctorName' : currentDoctor})

'''
For my own learning
from rdflib import Graph, URIRef

g = Graph()
g.parse("/Users/redwanwalid/Desktop/redwan/test.owl")

#for subj, pred, obj in g:
    #print(subj)
    # if (subj, pred, obj) not in g:
    #     raise Exception("It better be!")

makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#Elizabeth"
sub = URIRef(makeSub)

res = []
for triple in g.triples((sub,None,None)):
    p = triple[1].split('#')[1]
    #p = triple[1].split('#')
    #p = triple[1]
    #print(p)

    if (p.startswith('can')):
        permission = str(p[3])
        print(permission)
        if (permission == 'M'):
            field = str(p[9:])
            print(field)
        else:
            field = str(p[7:])

        if (field and permission):
            if field != 'VitalStats':
                res.append((field, permission))


print(res)
'''

'''
#Previous Search Function using Hashlib md5

def search(request):
    query = request.GET.get('query', '')

    hash_object = hashlib.md5(query.encode())
    UserToken = hash_object.hexdigest()

    patientData = []
    patients = PatientInfo.objects.all()

    with open('EHRindexFinal.data', 'rb') as filehandle:
        Indexes = pickle.load(filehandle)
        filehandle.close()

    for p in patients:
        for ind in Indexes:
            for i in range(1):
                # print(ind[i])
                for x in range(1,2):
                    if UserToken == ind[i] and p.patientName == ind[x] and p not in patientData:
                        # if p.patientName == ind[x]:
                        # print('There is a match')
                        # print(p.patientName)
                        # patientData.append(p)
                        # if p not in patientData:
                        print(p)
                        # print(p.patientName)
                        patientData.append(p)
                        # QueryResult.append(ind)

    return render(request, 'patientselectTESTcopy.html', {'doctorName' : loggedinUsers[-1], 'patientData' : patientData})

'''

'''
#Previous SWRL query
def runSWRL(doctorName, patientName):
    g = Graph()
    g.parse("/Users/redwanwalid/Desktop/redwan/django_test_r/EHROntology_v2.owl")
    #print(g)

    makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str(doctorName)
    #print(makeSub)
    sub 	= URIRef(makeSub)
    #print(sub)

    res = []
    for triple in g.triples((sub,None,None)):
        p 	= triple[1].split('#')[1]
        if (p.startswith('can')):
            permission = str(p[3])
            if (permission == 'M'):
                field = str(p[9:])
            else:
                field = str(p[7:])

            if (field and permission):
                if field != 'VitalStats':
                    res.append((field, permission))

    #print(res)

    return res

'''


