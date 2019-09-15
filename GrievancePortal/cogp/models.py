from django.db import models

class Student(models.Model):
	smail = models.EmailField(max_length=200,blank=False)
	spass = models.CharField(max_length=200,blank=False)

class Admin(models.Model):
	dname = models.CharField(max_length=200,blank=False)
	dpass = models.CharField(max_length=200,blank=False)

class Complaints(models.Model):
	cdept = models.CharField(max_length=200,blank=False)
	cquery = models.CharField(max_length=500,blank=False)
	cassignee = models.CharField(max_length=200,blank=False,default='')
	cstatus = models.CharField(max_length=200,default='Unresolved')
