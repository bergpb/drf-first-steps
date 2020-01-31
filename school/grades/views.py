from django.shortcuts import render
from django.http import JsonResponse
from school.grades.models import Student
from school.grades.serializers import StudentSerializers
from  rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
