from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dashboard/',views.dashboard),
    path('courses/',views.courses),
    path('signup/',views.signup),
    path('table/',views.table),
    path('viewstudent/',views.view_student),
    path('ragistration/',views.registration),
    path('login/', views.login),
    path('add_course/',views.add_Course)


]
