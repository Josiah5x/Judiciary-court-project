import email
from django.db import models

# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=100)  
    password = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)  

class ClientForm(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dateofbirth = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    file_id = models.CharField(max_length=100)
    complaint = models.CharField(max_length=1000)
    gender = models.CharField(max_length=100)
    date = models.DateField(max_length=100)

     
