from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Contact(models.Model):

    fname = models.CharField(max_length=144)
    lname = models.CharField(max_length=500)
   
    email = models.CharField(max_length=500)
    
    adress = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    
    state= models.TextField(max_length=222)
  
    date = models.DateField()
    