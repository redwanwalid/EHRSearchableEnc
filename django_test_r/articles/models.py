# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#models.Model to convert a class to a Model


class Article(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.TextField(max_length=254)
	body = models.TextField()
	likes = models.IntegerField()

class StaffInfo(models.Model):
	id = models.AutoField(primary_key=True)
	uid = models.TextField(max_length=25)
	username = models.TextField(max_length=254)
	password = models.TextField(max_length=25)
	role = models.TextField(max_length=50)
	certification = models.TextField(max_length=25)
	specialization = models.TextField(max_length=50)
	hward = models.TextField(max_length=25)

class PatientInfo(models.Model):
	id = models.AutoField(primary_key=True)
	patientName = models.TextField(max_length=254)
	patientPassword = models.TextField(max_length=25)
	purpose = models.TextField(max_length=500)
	doctorName = models.TextField(max_length=254)
	patientHward = models.TextField(max_length=25)


