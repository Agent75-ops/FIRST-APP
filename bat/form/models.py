from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser): 
    email = models.EmailField(max_length=256, unique=True)
    
    def __str__(self) :
        return self.username