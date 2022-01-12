from django.db import models
from django.db.models.base import Model

# Create your models here.


class Students(models.Model):

    stu_id    = models.IntegerField(primary_key=True)
    stu_name  = models.CharField(max_length=70)
    stu_email = models.EmailField(max_length=70)
    stu_pass  = models.CharField(max_length=70)
    stu_com   = models.CharField(max_length=40, default='Not Available')
