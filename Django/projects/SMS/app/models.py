from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    age  = models.IntegerField()
    fathername = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True)
    
    section_choices = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]
    
    section = models.CharField(choices=section_choices, max_length=100)
    class_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (5, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    ]
    
    standard = models.IntegerField(choices=class_choices)
    city    = models.CharField(max_length=70)
    
    
class Teacher(models.Model):
    name    = models.CharField(max_length=70)
    age     = models.IntegerField()
    subject = models.CharField(max_length=70)
    salary  = models.IntegerField()
    city    = models.CharField(max_length=70)
    