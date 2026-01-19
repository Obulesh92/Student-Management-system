from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='students/', null=True, blank=True)  # ✅ ADD THIS
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rollno = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    dob= models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
