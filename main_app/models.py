from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Space(models.Model):
  title: models.CharField(max_length=100)
  date: models.CharField(max_length=100)
  url: models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
