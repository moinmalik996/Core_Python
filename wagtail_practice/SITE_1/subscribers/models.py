from django.db import models

# Create your models here.


class Subscribers(models.Model):
    
    name  = models.CharField(max_length=70, blank=False, null=False, help_text='Enter Your Name')
    email = models.EmailField(max_length=70, blank=False, null=False, help_text='Enter Your Email')
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'