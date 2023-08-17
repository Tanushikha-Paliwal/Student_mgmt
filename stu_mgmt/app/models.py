from django.db import models,models

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
    sphone = models.IntegerField()
    scollege = models.CharField(max_length=200)
    sdegree = models.CharField(max_length=200)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourses = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.sname


class Teacher(models.Model):
    tname = models.CharField(max_length=200)
    temail = models.CharField(max_length=200)
    tpassword = models.CharField(max_length=200)
    tphone = models.IntegerField()
    join_date = models.DateField()
    t_qualification = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    tcourses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    # is_active = fields.BooleanField(default=True)
    
    def __str__(self):
        return self.tname