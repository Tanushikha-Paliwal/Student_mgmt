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


def update_view(request,c_id):
    data =   Courses.objects.get(id=c_id)
    return render(request,'updatecourse.html',{"data":data})

def update_course(request):
    if request.method == "POST":
        c_id = request.POST["c_id"]
        course_name = request.POST["CourseName"]
        fees = request.POST["CourseFees"]
        duration = request.POST["Duration"]
        comment = request.POST["CourseDesc"]
        Courses.objects.filter(id=c_id).update(course_name=course_name , fees=fees , duration=duration , comment=comment)
        return redirect('/courses/')
    

def delete(request,pk):
    Courses.objects.filter(id=pk).delete()
    return redirect("/courses/")

def view_student(request):
    stu = AddStudent.objects.all()
    add_Course = Courses.objects.all()
    redirect('viewstudents')
    return render(request, 'viewstudents.html' , {'stu':stu , 'add_Course':add_Course})

def add_student(request):
    if request.method == "POST":
        st_name = request.POST.get['sname']
        st_email = request.POST.get['semail']
        st_phone = request.POST.get['phone']
        st_college = request.POST.get['college']
        st_degree = request.POST.get['degree']
        st_addCourse_id = request.POST.get['course']
        total_amount = request.POST.get['total_amt']
        paid_amount = request.POST.get['paid_amt']
        due_amount = request.POST.get['due_amt']
        st_course = Courses.objects.get(id=st_addCourse_id)
        if AddStudent.objects.filter(semail=st_email).exists():
            messages.error(request , "Email Already Exists")
            return redirect('add_student')
        elif AddStudent.objects.filter(sphone=st_phone).exists():
            messages.error(request , "Mobile Number Already Exists")
            return redirect('add_student')
        else:
            AddStudent.objects.create(sname=st_name , semail=st_email , sphone=st_phone , scollege=st_college , sdegree=st_degree , scourses=st_course , total_amount=total_amount , paid_amount=paid_amount , due_amount=due_amount)
            messages.success(request , "Student Addedd Successfully.......")
            stu = AddStudent.objects.all()
            add_Course = Courses.objects.all()
            return render(request,'viewstudents.html', {'stu':stu , 'add_Course':add_Course})
    else:
        AddStudent.objects.create(sname=st_name , semail=st_email , sphone=st_phone , scollege=st_college , sdegree=st_degree , scourses=st_course , total_amount=total_amount , paid_amount=paid_amount , due_amount=due_amount)
        messages.success(request , "Student Addedd Successfully.......")
        stu = AddStudent.objects.all()
        add_Course = Courses.objects.all()
        return render(request,'viewstudents.html', {'stu':stu , 'add_Course':add_Course})


    
    