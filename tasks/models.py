from django.conf import settings
from django.db import models

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

