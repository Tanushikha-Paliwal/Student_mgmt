from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)


class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    fees = models.FloatField(max_length=200)
    comment = models.TextField()
    duration = models.CharField(max_length=150)

