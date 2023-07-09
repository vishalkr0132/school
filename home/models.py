from django.db import models
from django.contrib.auth.models import User
from msilib.schema import Class

# Create your models here.

class Register(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=150)
    Password = models.CharField(max_length=200)
    Confirm_Password = models.CharField(max_length=200)

    def __str__(self):
        return self.Email
    
class Contacts(models.Model):
    Full_Name = models.CharField(max_length=150)
    Subject = models.CharField(max_length=250)
    Mobile = models.IntegerField()
    Email = models.EmailField(max_length=250)
    Message = models.CharField(max_length=250)
    
    def __str__(self):
        return self.Full_Name