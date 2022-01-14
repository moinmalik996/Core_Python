from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    post_title = models.CharField(max_length=70)
    post_cat   = models.CharField(max_length=70)
    post_date  = models.DateField()
    
    """
    ----------------models.PROTECT-------------------
    
    SUPPOSE YOU WANT TO RAISE ERROR WHEN A USER IS GOING
    TO DELETE WITH ITS DATA(POSTS in this case) THEN 
    
    models.PROTECT WILL BE USED
    
    DJANGO WILL NOT ALLOW YOU TO DELETE USER UNTILL ITS DATA
    IS NOT DELETED.
    
    
    """
    
    """
    ----------------models.SET_NULL-------------------
    
    IF YOU DELETE THE USER THEN THE POSTS MADE BY THE USER WILL
    STILL THERE WITH FOREIGNKEY SET TO NULL.
    
    YOU HAVE TO PASS NULL = TRUE BECAUSE ITS NULL = FALSE BY DEFAULT.
    
    """
    
    
