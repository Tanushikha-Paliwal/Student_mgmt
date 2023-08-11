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
    if request.method == "POST":
        course_name = request.POST["CourseName"]
        fees = request.POST["CourseFees"]
        duration = request.POST["Duration"]
        comment = request.POST["CourseDesc"]
        Courses.objects.create(
            course_name=course_name, fees=fees, duration=duration, comment=comment
        )
        return redirect("/courses/")


def update_view(request, c_id):
    data = Courses.objects.get(id=c_id)
    return render(request, "updatecourse.html", {"data": data})


def update_course(request):
    if request.method == "POST":
        c_id = request.POST["c_id"]
        course_name = request.POST["CourseName"]
        fees = request.POST["CourseFees"]
        duration = request.POST["Duration"]
        comment = request.POST["CourseDesc"]
        Courses.objects.filter(id=c_id).update(
            course_name=course_name, fees=fees, duration=duration, comment=comment
        )
        return redirect("/courses/")


def delete(request, pk):
    Courses.objects.filter(id=pk).delete()
    return redirect("/courses/")


def view_student(request):
    stu = AddStudent.objects.all()
    addcourses = Courses.objects.all()
    redirect("/viewstudents/")
    return render(request, "viewstudents.html", {"stu": stu, "addcourses": addcourses})


def add_student(request):
    if request.method == "POST":
        stu_name = request.POST.get("Name")
        stu_email = request.POST.get("Email")
        stu_mobile = request.POST.get("Mobile")
        stu_college = request.POST.get("College")
        stu_degree = request.POST.get("Degree")
        stu_addcourse_id = request.POST.get("course")
        total_amount = request.POST.get("qty")
        paid_amount = request.POST.get("cost")
        due_amount = request.POST.get("DueAmount")
        stu_course = Courses.objects.get(id=stu_addcourse_id)
        if AddStudent.objects.filter(semail=stu_email).exists():
            messages.error(request, "Email id already exists")
            return redirect("/viewstudents/")

        elif AddStudent.objects.filter(sphone=stu_mobile).exists():
            messages.error(request, "Mobile Number already exists")
            return redirect("/viewstudents/")
        else:
            AddStudent.objects.create(
                sname=stu_name,
                semail=stu_email,
                sphone=stu_mobile,
                scollege=stu_college,
                sdegree=stu_degree,
                scourses=stu_course,
                total_amount=total_amount,
                paid_amount=paid_amount,
                due_amount=due_amount,
            )
            messages.success(request, "Student Added Successfully!!")
            stu = AddStudent.objects.all()
            addcourses = Courses.objects.all()
            return render(
                request,
                "viewstudents.html",
                {
                    "stu": stu,
                    "addcourses": addcourses,
                },
            )
    else:
        stu = AddStudent.objects.all()
        addcourses = Courses.objects.all()
        return render(
            request, "viewstudents.html", {"stu": stu, "addcourses": addcourses}
        )


def update_student_view(request, s_id):
    data = AddStudent.objects.get(id=s_id)
    addcourses = Courses.objects.all()
    redirect("/studentupdateview/")
    return render(
        request, "studentupdate.html", {"data": data, "addcourses": addcourses}
    )


def update_student(request):
    if request.method == "POST":
        s_id = request.POST["s_id"]
        sname = request.POST["Name"]
        semail = request.POST["Email"]
        sphone = request.POST["Mobile"]
        scollege = request.POST["College"]
        sdegree = request.POST["Degree"]
        total_amount = request.POST["qty"]
        paid_amount = request.POST["cost"]
        due_amount = request.POST["DueAmount"]
        # scourses = request.POST["course"]

        AddStudent.objects.filter(id=s_id).update(
            sname=sname,
            semail=semail,
            sphone=sphone,
            scollege=scollege,
            sdegree=sdegree,
            total_amount=total_amount,
            paid_amount=paid_amount,
            due_amount=due_amount,
            # scourses=scourses,
        )
        return redirect("/addstudent/")
