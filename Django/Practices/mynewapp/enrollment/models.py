from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class StudentData(models.Model):
    name     = models.CharField(max_length=70)
    email    = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)