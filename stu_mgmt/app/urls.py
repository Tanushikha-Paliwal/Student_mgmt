from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("dashboard/", views.dashboard),
    path("courses/", views.courses),
    path("signup/", views.signup),
    path("table/", views.table),
    path("viewstudent/", views.view_student),
    path("ragistration/", views.registration),
    path("login/", views.login),
    path("add_course/", views.add_Course),
    path("updateview/<int:c_id>/", views.update_view),
    path("updatecourse/", views.update_course),
    path("delete/<int:pk>/", views.delete, name="delete_course"),
    path("viewstudents/", views.view_student),
    path("addstudent/", views.add_student),
    path(
        "studentupdateview/<int:s_id>/",
        views.update_student_view,
        name="studentupdateview",
    ),
    path("updatestudent/", views.update_student),
    path('deletestudent/<int:pk>/',views.delete_student , name="delete_student"),
    path('search/',views.search_student , name='search'),
    path('search_courses/',views.search_courses , name='search_courses'),
    path('viewteacher/',views.teachers_view),
    path('teachersview/',views.view_teachers),
    path('addteachers/',views.add_teacher),
    path('updateviewteacher/<int:t_id>/',views.update_teacher_view),
    path('updateteacher/',views.update_teacher),
    path('delete/<int:pk>/',views.delete_teacher , name="delete_teacher"),
    path('search_teachers/',views.search_teacher , name='search_teachers'),

]
