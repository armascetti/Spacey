from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User 
# Create your models here.

class Space(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField()
  url = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.date}'

  def get_absolute_url(self):
    return reverse("pics_detail", kwargs={"pic_id": self.id})