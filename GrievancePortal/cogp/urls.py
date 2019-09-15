from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('uls', views.uls, name='uls'),
	path('uls/signup', views.usignup, name='usignup'),
	path('uls/login', views.ulogin, name='ulogin'),
	path('alogin', views.alogin, name='alogin'),
	path('uls/register', views.register, name='register'),
	path('uls/signin', views.signin, name='signin'),
	path('asignin', views.asignin, name='asignin'),
	path('postc', views.postc, name='postc'),
	path('viewc', views.viewc, name='viewc'),
	path('ahome/resolve', views.resolve, name='resolve'),
	path('complaint/postc', views.cpostc, name='cpostc'),
]