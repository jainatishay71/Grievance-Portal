from django.http import HttpResponse
from django.shortcuts import render, redirect
from cogp.models import Student,Admin,Complaints
# from django.models import User,authenticate

def index(request):
	return render(request,'cogp/home.html',{})

def uls(request):
	return render(request,'cogp/uls.html',{})

def alogin(request):
	return render(request,'cogp/alogin.html',{})

def usignup(request):
	return render(request,'cogp/usignup.html',{})

def ulogin(request):
	return render(request,'cogp/ulogin.html',{})

def register(request):
	if request.method=='POST':
		email=request.POST['Email']
		password=request.POST['Password']

		try:
			ans=Student.objects.get(smail=email)
		except:
			ans=None
		if ans is None:
			obj=Student()
			obj.smail=email
			obj.spass=password
			obj.save()
			context={'smail':email}
			return render(request,'cogp/ulogin.html',context)
		else:
			context={'msg':'User already registered with this Mail-Id',}
			return render(request,'cogp/usignup.html',context)
	elif request.method=='GET':
		return render(request,'cogp/usignup.html',{})

def signin(request):
	if request.method=='POST':
		email=request.POST['Email']
		password=request.POST['Password']
		try:
			ans=Student.objects.get(smail=email)
		except:
			ans=None
		if ans is not None:
			if ans.spass==password:
				context={
				'email':ans.smail,
				}
				return render(request,'cogp/uhome.html',context)
			else:
				context={
				'msg':'give correct details',
				}
				return render(request,'cogp/ulogin.html',context)
		else:
			context={
			'msg':'no such registered user',
			}
			return render(request,'cogp/ulogin.html',context)
	else:
		return render(request,'cogp/ulogin.html',context)

def asignin(request):
	if request.method=='POST':
		dept=request.POST['Department']
		password=request.POST['Password']
		try:
			ans=Admin.objects.get(dname=dept)
		except:
			ans=None
		if ans is not None:
			if ans.dpass==password:
				listt = Complaints.objects.filter(cdept=dept)
				context={
					'listt':listt,
				}
				return render(request,'cogp/ahome.html',context)
			else:
				context={
				'msg':'give correct details',
				}
				return render(request,'cogp/alogin.html',context)
		else:
			context={
			'msg':'no such registered user',
			}
			return render(request,'cogp/alogin.html',context)
	else:
		return render(request,'cogp/alogin.html',context)

def postc(request):
	return render(request,'cogp/complaint.html',{})

def viewc(request):
	listt = Complaints.objects.all()
	context = {
		'listt':listt,
	}
	return render(request,'cogp/history.html',context)

def cpostc(request):
	if request.method=='POST':
		dept=request.POST['Department']
		query=request.POST['Query']

		obj=Complaints()
		obj.cdept=dept
		obj.cquery=query
		obj.save()
		context={'cquery':query}
		return render(request,'cogp/uhome.html',context)
	elif request.method=='GET':
		return render(request,'cogp/uhome.html',{})

def resolve(request):
	if request.method=='POST':
		cquery=request.POST['cquery']
		assignee=request.POST['assignee']
		status=request.POST['status']
		obj=Complaints.objects.get(cquery=cquery)
		obj.assignee=assignee
		obj.status=status
		obj.save()
		listt = Complaints.objects.filter(cdept=dept)
		context={
			'listt':listt,
		}
		return render(request,'cogp/ahome.html',context)
	elif request.method=='GET':
		return render(request,'cogp/ahome.html',{})