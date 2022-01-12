from django.db import models

# Create your models here.

class StudentData(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    pass_w = models.CharField(max_length=70)