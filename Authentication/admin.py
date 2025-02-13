from django.contrib import admin
from Authentication.models import Student

# # Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id_number','name','class_room']

admin.site.register(Student,StudentAdmin)


