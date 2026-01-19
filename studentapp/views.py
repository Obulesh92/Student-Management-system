from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def student_login(request):
    if request.method == 'POST':
        rollno = request.POST.get('rolno')
        password = request.POST.get('password')

        student = Student.objects.filter(
            rollno=rollno,
            password=password
        ).first()

        if student:
            # store logged-in student id in session
            request.session['student_id'] = student.id

            return redirect('student_dashboard')
        else:
            return render(request, 'Student/student_login.html', {
                'message': 'Invalid credentials'
            })

    return render(request, 'Student/student_login.html')
def student_dashboard(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)

    return render(request, 'Student/student_dashboard.html', {
        'student': student
    })


def student_logout(request):
    return redirect('student_login')

def student_profile(request):
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    return render(request,"Student/student_profile.html", {'student': student})