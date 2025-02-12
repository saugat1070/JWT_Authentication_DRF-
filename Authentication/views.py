from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Authentication.models import Student
from Authentication.serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def api_root(request,format=None):
    return Response(status=status.HTTP_200_OK)

class StudentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request,format=None):
        queary = Student.objects.all()
        serializer = StudentSerializer(queary,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        queary = Student.objects.all()
        serializer = StudentSerializer(queary,data = request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
