from django.urls import path
from .api import *

urlpatterns = [
    path('',RegistrationViewSet.as_view()),
    path('addcourse/',CourseViewSet.as_view()),
    path('addstu/',AddStudentViewSet.as_view()),
    path('teacher/',TeacherViewSet.as_view())
]

