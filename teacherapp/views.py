from django.shortcuts import render,redirect
from .models import Teacher
# Create your views here.
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Teacher.objects.filter(username=username, password=password).exists():
            return redirect('teacher_dashboard')
        else:
            return render(request, 'Teacher/teacher_login.html', {'message': 'Invalid credentials'})
    return render(request, 'Teacher/teacher_login.html')

def teacher_dashboard(request):
    return render(request, 'Teacher/teacher_dashboard.html')

def teacher_logout(request):
    return redirect('teacher_login')