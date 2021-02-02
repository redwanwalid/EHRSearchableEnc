"""django_test_r URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from articles import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.hello, name='home'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('hello_template/', views.hello_template, name='hello_template'),
    path('hello_template_simple/', views.hello_template_simple, name='hello_template_simple'),
    path('hello/', views.hello, name='hello'),
    path('staffsignup/', views.staffsignup),
    path('staffsignup_view/', views.staffsignup_view),
    path('stafflogin/', views.stafflogin),
    path('stafflogin_view/', views.stafflogin_view),
    path('patientsignup/', views.patientsignup),
    path('patientsignup_view/', views.patientsignup_view),
    path('patientlogin/', views.patientlogin),
    path('patientlogin_view/', views.patientlogin_view),
    path('getselectedpatient/', views.getSelectedPatient),
    path('getselectedpatient/LabResults.txt/', views.LabResults),
    path('getselectedpatient/Diagnoses.txt/', views.Diagnoses),
    path('getselectedpatient/Medication.txt/', views.Medication),
    path('getselectedpatient/Prescription.txt/', views.Prescription),
    path('getselectedpatient/DoctorNotes.txt/', views.DoctorNotes),
    path('getselectedpatient/Allergies.txt/', views.Allergies),
    path('getselectedpatient/BillingInfo.txt/', views.BillingInfo),
    path('getselectedpatient/ImmunizationDates.txt/', views.ImmunizationDates),
    path('saveedits/', views.saveEdits),
    path('saveedits/LabResults.txt/', views.LabResults),
    path('saveedits/Diagnoses.txt/', views.Diagnoses),
    path('saveedits/Medication.txt/', views.Medication),
    path('saveedits/Prescription.txt/', views.Prescription),
    path('saveedits/DoctorNotes.txt/', views.DoctorNotes),
    path('saveedits/Allergies.txt/', views.Allergies),
    path('saveedits/BillingInfo.txt/', views.BillingInfo),
    path('saveedits/ImmunizationDates.txt/', views.ImmunizationDates),
    path('getselectedpatient/explain.txt/', views.explain),
    path('patientlogin_view/LabResults.txt/', views.LabResults),
    path('patientlogin_view/ImmunizationDates.txt/', views.ImmunizationDates),
    path('patientlogin_view/BillingInfo.txt/', views.BillingInfo),
    path('patientlogin_view/Allergies.txt/', views.Allergies),
    path('patientlogin_view/DoctorNotes.txt/', views.DoctorNotes),
    path('patientlogin_view/Prescription.txt/', views.Prescription),
    path('patientlogin_view/Medication.txt/', views.Medication),
    path('patientlogin_view/Diagnoses.txt/', views.Diagnoses),


    path('home/staffsignup/', views.staffsignup),
    path('home/staffsignup_view/', views.staffsignup_view),
    path('home/stafflogin/', views.stafflogin),
    path('home/stafflogin_view/', views.stafflogin_view),
    path('home/patientsignup/', views.patientsignup),
    path('home/patientsignup_view/', views.patientsignup_view),
    path('home/patientlogin/', views.patientlogin),
    path('home/patientlogin_view/', views.patientlogin_view),
    path('searchEHR/', views.search),
    url(r'stafflogin/$', views.stafflogin),
    url(r'staffsignup/$', views.staffsignup),
    url(r'patientlogin/$', views.patientlogin),
    url(r'patientsignup/$', views.patientsignup)

]