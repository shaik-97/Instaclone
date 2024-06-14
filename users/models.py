import datetime

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

#BigAutoField = int
#CharFiled - varchar
#Boolean Field
#Decimal_places - Float
# ForeignKey - ForeignKey

# Create your models here.
print("This is from models.py")

""" THis class has been commented bcz there's already a class/model called 'User' supported by django"""
# class User(models.Model):
#     name = models.CharField(max_length=255, null=False)
#     email = models.EmailField(max_length=255, null=False, unique=True)
#     ph_no = models.CharField(max_length=11, unique=True)
#     date_joined = models.DateTimeField(auto_now=True) # whenever this model gets created date_joined will be set to that date
#     updated_on = models.DateTimeField(auto_now=True) # whenever this model "User "gets updated, update update_on field
#     is_verified = models.BooleanField(default=False)
#     password = models.CharField(max_length=255, null=False)


class TimeStamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # This meta class and abstract=true is to tell django that do not create table of main class TimeStamp as these are common methods
    # which will be used across other classes
    class Meta:
        abstract = True

class UserProfile(TimeStamp):
    DEFAULT_PROFILE_PIC = "https://mywebsite.com/placeholder.png"

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    profile_pic_url = models.ImageField(max_length=255, default=DEFAULT_PROFILE_PIC)
    bio = models.CharField(max_length=255, blank=True) # blank-true empty string is allowed
    is_verified = models.BooleanField(default=False)

