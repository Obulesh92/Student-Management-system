from django.shortcuts import render,redirect
from .models import Admin, Contact
    
def home(request):
    return render(request, 'home.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Admin.objects.filter(username=username, password=password).exists():
            return redirect('admin_dashboard')
    return render(request, 'Admin/admin_login.html')

def admin_dashboard(request):
    return render(request, 'Admin/admin_dashboard.html')

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