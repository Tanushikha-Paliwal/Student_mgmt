from .. models import *
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class AddStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddStudent
        fields = '__all__'

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'