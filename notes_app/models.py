from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(User, default='',on_delete=models.CASCADE)

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List, default='',on_delete=models.CASCADE)
