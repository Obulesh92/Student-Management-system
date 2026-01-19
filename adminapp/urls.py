from django.urls import path
from .views import edit_student,home, admin_login, admin_dashboard, contact_us, logout, student_manage, add_student, delete_student

urlpatterns = [
    # Define your adminapp URL patterns here
    path("",home,name="home"),
    path("admin_login/",admin_login,name="admin_login"),
    path("admin_dashboard/",admin_dashboard,name="admin_dashboard"),
    path("contact/",contact_us,name="contact"),
    path("logout/",logout,name="logout"),
    path("student_manage/",student_manage,name="student_manage"),
    path("add_student/",add_student,name="add_student"),
    path("delete_student/<int:pk>/",delete_student,name="delete_student"), 
    path("edit_student/<int:pk>/",edit_student,name="edit_student"),  
]