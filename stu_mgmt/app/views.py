from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from django.contrib import messages
from django.db.models import Q

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


def teachers_view(request):
    return render(request, "teachers.html")


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



def delete_student(request,pk):
    AddStudent.objects.filter(id=pk).delete()
    return redirect('/addstudent/')


def search_student(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains=q)) | Q(Q(semail__icontains=q)) | Q(Q(sphone__icontains=q))
        stu = AddStudent.objects.filter(multiple_q)
    else:
        stu = AddStudent.objects.all()
    context = {'stu':stu}
    return render(request,'viewstudents.html',context)


def search_courses(request):
    if 'c' in request.GET:
        c = request.GET['c']
        multiple_c = Q(Q(course_name__icontains=c))
        course_obj = Courses.objects.filter(multiple_c)
    else:
        course_obj = Courses.objects.all()
    context = {'course_obj':course_obj}
    return render(request,'courses.html',context)





def view_teachers(request):
    teacher = Teacher.objects.all()
    addcourses = Courses.objects.all()
    redirect("/teachersview/")
    return render(request, "teachers.html",{"teacher":teacher , "addcourses":addcourses})

def add_teacher(request):
    if request.method == "POST":
        t_name = request.POST.get("name")
        t_email = request.POST.get("email")
        t_password = request.POST.get("password")
        t_phone = request.POST.get("phone")
        t_join_date = request.POST.get("date")
        t_qualification = request.POST.get("qualification")
        t_courses_id = request.POST.get("course")
        t_emp_id = request.POST.get("emp_id")
        t_gender = request.POST.get("gender")
        t_courses = Courses.objects.get(id=t_courses_id)
        if Teacher.objects.filter(tphone=t_phone).exists():
            messages.error(request , "Teacher's Phone Number Already Exists")
            return redirect("/teachersview/")
        elif Teacher.objects.filter(temail=t_email).exists():
            messages.error(request , "Teacher's Email Already Exists")
            return redirect("/teachersview/")
        else:
            Teacher.objects.create(
                tname = t_name ,
                temail = t_email ,
                tpassword = t_password , 
                tphone = t_phone , 
                join_date = t_join_date , 
                t_qualification = t_qualification ,
                employee_id = t_emp_id ,
                tcourses = t_courses ,
                gender = t_gender
            )
            messages.success(request , "Teacher added sucessfully..!!!")
            teacher = Teacher.objects.all()
            addcourses = Courses.objects.all()
            return render(request, "teachers.html",{"teacher":teacher , "addcourses":addcourses})
        

def update_teacher_view(request,t_id):
    data = Teacher.objects.get(id=t_id)
    addcourses = Courses.objects.all()
    return redirect(request , "teacherupdate.html", {"data":data , "addcourses":addcourses})

def update_teacher(request):
    if request.method == "POST":
        t_id = request.POST['t_id']
        tname = request.POST['name']
        temail = request.POST['email']
        tphone =  request.POST['phone']
        join_date = request.POST['date']
        t_qualification = request.POST['qualification']
        employee_id = request.POST['emp_id']
        gender = request.POST['gender']

        Teacher.objects.filter(id=t_id).update(
            tname = tname,
            temail = temail,
            tphone =tphone ,
            join_date = join_date ,
            t_qualification = t_qualification ,
            employee_id =employee_id ,
            gender = gender
        )
        return redirect("/addteachers/")
    
def delete_teacher(request,pk):
    Teacher.objects.filter(id=pk).delete()
    return redirect("/addteachers/")

def search_teacher(request):
     if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(tname__icontains=q)) | Q(Q(temail__icontains=q)) | Q(Q(tphone__icontains=q))
        stu = Teacher.objects.filter(multiple_q)
     else:
        stu = Teacher.objects.all()
     context = {'stu':stu}
     return render(request,'teachers.html',context)
