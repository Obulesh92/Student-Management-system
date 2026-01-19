from django.shortcuts import render,redirect
from .models import Admin, Contact
from django.shortcuts import get_object_or_404
from studentapp.models import Student
    
def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Admin.objects.filter(username=username, password=password).exists():
            return redirect('admin_dashboard')
        else:
            return render(request, 'Admin/admin_login.html', {'message': 'Invalid username or password'})    
    return render(request, 'Admin/admin_login.html')

def admin_dashboard(request):
    return render(request, 'Admin/admin_dashboard.html')
def logout(request):
    return redirect('admin_login')

def contact_us(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        # Save contact form data to the database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('home')
    return render(request, 'home.html')
def student_manage(request):
    return render(request, 'Admin/student_manage.html', {'students': Student.objects.all()})
def add_student(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        password = request.POST.get('password')
        rollno = request.POST.get('rollno')
        course=request.POST.get('course')
        branch = request.POST.get('branch')
        year=request.POST.get('year')
        email = request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        
        # Save new student data to the database
        if not Student.objects.filter(rollno=rollno).exists():
            student = Student(
                image=image if image else None,
                name=name, 
                password=password,
                rollno=rollno,
                course=course,
                branch=branch,
                year=year,
                email=email, 
                phone=phone,
                gender=gender,
                dob=dob,
                address=address)
            student.save()
            return redirect('student_manage')
    return render(request, 'Admin/student_manage.html')

def delete_student(request, pk):
    try:
        student = get_object_or_404(Student, id=pk)
        student.delete()
    except Student.DoesNotExist:
        pass
    return redirect('student_manage')
def edit_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        student.rollno = request.POST.get('rollno')
        student.name = request.POST.get('name')
        student.branch = request.POST.get('branch')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.phone = request.POST.get('phone')
        student.gender = request.POST.get('gender')
        student.dob = request.POST.get('dob')
        student.address = request.POST.get('address')
        student.save()

        return redirect('student_manage')

    return render(request, 'Admin/edit_student.html', {'student': student})