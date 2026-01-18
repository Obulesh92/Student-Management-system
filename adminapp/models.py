from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self):
        return self.name