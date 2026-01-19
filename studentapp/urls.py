from django.urls import path
from .views import student_login,student_logout,student_dashboard,student_profile
urlpatterns = [
    path('login/', student_login, name='student_login'),
    path('logout/', student_logout, name='student_logout'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path("profile/",student_profile,name="student_profile")
]