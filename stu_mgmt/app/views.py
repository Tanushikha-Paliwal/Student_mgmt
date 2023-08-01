from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from django.contrib import messages

# Create your views here.


def courses(request):
    course_obj = Courses.objects.all()
    return render(request, "courses.html", {"course_obj": course_obj})


def dashboard(request):
    return render(request, "dashboard.html")


def index(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "sign-up.html")


def table(request):
    return render(request, "tables.html")


def view_student(request):
    return render(request, "viewstudents.html")


def registration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if Student.objects.filter(email=email).exists():
            return HttpResponse("User already exists")
        else:
            Student.objects.create(email=email, name=name, password=password)
            return redirect("/")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        user_passsword = request.POST["password"]
        if Student.objects.filter(email=email).exists():
            temp = Student.objects.get(email=email)
            password = temp.password
            if check_password(user_passsword, password):
                return redirect("/dashboard/")
            else:
                return HttpResponse("password incorrect")
        else:
            return HttpResponse("Email not registerd")


def add_Course(request):
    if request.method == 'POST':
        course_name = request.POST["CourseName"]
        fees = request.POST["CourseFees"]
        duration = request.POST["Duration"]
        comment = request.POST["CourseDesc"]
        Courses.objects.create(course_name=course_name,fees=fees
                               ,duration=duration,comment=comment)
        return redirect("/courses/")


