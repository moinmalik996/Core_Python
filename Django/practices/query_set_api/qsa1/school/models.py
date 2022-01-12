from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks= models.IntegerField()
    pass_date = models.DateField()
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=70)
    enum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField(null=False)
    join_date = models.DateField()
    