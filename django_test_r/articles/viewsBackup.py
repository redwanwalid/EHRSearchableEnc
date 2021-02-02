# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from rdflib import Graph, URIRef
from articles.models import StaffInfo
from articles.models import PatientInfo

loggedinUsers = []
fieldsWithPermissions = []
allowedFiles = []

def hello(request):
	name = "Maithilee"
	html = "<html><body>Hi %s, this seems to have worked!</body></html>" %name
	return HttpResponse(html)

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
	return render_to_response('hello.html', {'fname':fname, 'lname':lname})

def home(request):
	return render(request, 'home.html')

def staffsignup(request):
	return render_to_response('staffsignup.html')

def stafflogin(request):
	return render_to_response('stafflogin.html') 

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
	return render_to_response('stafflogin.html')

def stafflogin_view(request):
	uid = request.GET.get('uid', '')
	username = request.GET.get('username', '')
	password = request.GET.get('password', '')



	staffData = StaffInfo.objects.all()

	for sD in staffData:
		if ((sD.uid == uid) and (sD.username == username) and (sD.password == password)):
			loggedinUsers.append(username)

			# If login creds are correct, then filter patients of the same ward
			patientData = []
			patients = PatientInfo.objects.all()

			for p in patients:
				# print (p.patientHward, sD.hward)
				if (p.patientHward == sD.hward):
					# print ("here")	
					patientData.append(p)

			return render_to_response('patientselect.html', {'doctorName' : username, 'patientData' : patientData})

	html = "<html><body> Invalid login credentials provided..! <p> Please go back and try login using your credentials or create a new account by signing up.</p> </body> </html>"
	return HttpResponse(html)

def patientsignup(request):
	return render_to_response('patientsignup.html')

def patientlogin(request):
	return render_to_response('patientlogin.html')

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
	return render_to_response('patientlogin.html')

def patientlogin_view(request):
	patientName = request.GET.get('patientName', '')
	patientPassword = request.GET.get('patientPassword', '')

	patientData = PatientInfo.objects.all()

	for pD in patientData:
		# print (str(sD.uid), sD.uid)
		# print (str(sD.username), sD.username)
		# print (str(sD.password), sD.password)
		if ((pD.patientName == patientName) and (pD.patientPassword == patientPassword)):
			loggedinUsers.extend(['None', patientName])
			patientEHRfields = ['Diagnoses', 'Medication', 'Prescription', 'Allergies', 'LabResults', 'ImmunizationDates', 'DoctorNotes', 'BillingInfo']			
			return render_to_response("patientehrview.html", {'allowedFields':patientEHRfields, 'patientName' : patientName})

	return render_to_response("patientlogin.html", {'error_flag' : True})
	# html = "<html><body> Invalid login credentials provided..! <p> Please go back and try login using your credentials or create a new account by signing up.</p> </body> </html>"
	# return HttpResponse(html)	

def runSWRL(doctorName, patientName):
	g = Graph()
	g.parse("/home/maithilee/Documents/Fall2017/Thesis/EHROntology.owl")

	# pred 	= URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
	makeSub = "http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#" + str(doctorName)
	sub 	= URIRef(makeSub)
	# obj 	= URIRef("http://www.semanticweb.org/umbcknacc/ontologies/2017/10/untitled-ontology-3#SeniorDoctor")

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
				res.append((field, permission))

	return res

def getSeletedPatient(request):
	selectedPatient = request.GET.get('checks')
	currentDoctor = loggedinUsers[0]
	loggedinUsers.append(selectedPatient)

	print (currentDoctor, selectedPatient)

	
	fieldsWithPermissions.extend(runSWRL(currentDoctor, selectedPatient))
	print (fieldsWithPermissions)

	if (fieldsWithPermissions == []):
		return HttpResponse("Access Denied!")

	else:
		allowedFiles.extend([fwp[0] for fwp in fieldsWithPermissions])
		print (allowedFiles)
		return render_to_response("patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : selectedPatient, 'doctorName' : currentDoctor})

def LabResults(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/LabResults.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)

def Prescription(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/Prescription.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)

def Medication(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/Medication.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)

def Allergies(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/Allergies.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)

def DoctorNotes(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/DoctorNotes.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)


def Diagnoses(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/Diagnoses.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)


def ImmunizationDates(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/ImmunizationDates.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)


def BillingInfo(request):
	currentPatient = loggedinUsers[1]
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/BillingInfo.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)

# @csrf_exempt
def saveEdits(request):
	currentPatient = loggedinUsers[1]
	currentDoctor = loggedinUsers[0]

	editField = request.GET.get('select')
	print (str(editField))

	newEdits = request.GET.get('inputEdit')
	print (str(newEdits))

	print (allowedFiles)
	editFieldIndex = allowedFiles.index(editField)
	print (editFieldIndex)
	print (fieldsWithPermissions)
	fieldpermission = fieldsWithPermissions[editFieldIndex][1]
	print (fieldpermission)

	if fieldpermission != 'M':
		html = "<html><body> You do not have edit access"
		return HttpResponse(html)

	else:
		filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/' + editField + '.html'
		f = open(filepath, 'a+')
		f.write("<p>")
		f.write(newEdits)
		f.write("</p>")
		return render_to_response("patientehrdetails.html", {'allowedFields':allowedFiles, 'patientName' : currentPatient, 'doctorName' : currentDoctor})

def explain(request):
	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/accessExplain.html'
	f = open(filepath, 'r')
	filecontents = f.read()

	return HttpResponse(filecontents)
	# return render_to_response('home.html')

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
	# 	filepath = '/home/maithilee/Documents/Fall2017/Thesis/Django/django_test/PatientEHRs/' + currentPatient + '/' + field + '.html'
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







