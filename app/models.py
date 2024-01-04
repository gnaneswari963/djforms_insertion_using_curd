from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)



class Student(models.Model):
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    sgender=models.CharField(max_length=100)
    scourse=models.CharField(max_length=100)
    saddress=models.CharField(max_length=100)
    spassword=models.CharField(max_length=100)
    
    