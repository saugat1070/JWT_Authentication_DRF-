from rest_framework import serializers
from Authentication.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id_number','name','class_room']