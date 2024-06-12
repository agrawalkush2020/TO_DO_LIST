from django.db import models
from django import forms
from .forms import SignUpForm

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique = True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    value = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

    def __str__(self):
        return self.value