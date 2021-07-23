from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.urls import reverse

class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    phone_no = models.CharField(max_length= 20,blank=True,null=True)


    def _str__(self):
        return self.username
