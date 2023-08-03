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

class AddStudent(models.Model):
    sname = models.CharField(max_length=200)
    semail = models.CharField(max_length=200)
    sphone = models.IntegerField(max_length=10)
    scollege = models.CharField(max_length=200)
    sdegree = models.CharField(max_length=200)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField()
    scourses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sname