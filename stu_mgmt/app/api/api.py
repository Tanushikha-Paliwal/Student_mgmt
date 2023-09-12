from .. models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics


# Student Registration API

class RegistrationViewSet(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class CourseViewSet(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializers

class AddStudentViewSet(generics.CreateAPIView):
    queryset = AddStudent.objects.all()
    serializer_class = AddStudentSerializers

class TeacherViewSet(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers