from django.db import models

# Create your models here.

class Feedback(models.Model):
    customername = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    ordernumber = models.CharField(max_length=15)
    message = models.CharField(max_length=100)
    
    