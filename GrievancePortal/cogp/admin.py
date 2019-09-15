from django.contrib import admin

from .models import Student,Admin,Complaints

# Register your models here.

admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Complaints)