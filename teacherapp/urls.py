from django.urls import path
from .views import teacher_dashboard, teacher_login, teacher_logout
urlpatterns = [
    path('login/', teacher_login, name='teacher_login'),
    path('dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('logout/', teacher_logout, name='teacher_logout'),
]