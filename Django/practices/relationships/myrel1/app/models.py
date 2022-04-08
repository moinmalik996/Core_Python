from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    
    p_name = models.CharField(max_length=70)
    p_cat  = models.CharField(max_length=100)
    p_date = models.DateField()

