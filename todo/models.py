from django.db import models
from django import forms
from .forms import SignUpForm

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value
    
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique = True)
    password=models.CharField(max_length=50)

    def __str__(self)->str:
        return self.username
     



