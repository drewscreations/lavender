from django.db import models
import re
from datetime import date, datetime
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="must have more than 2 characters in first name"
        if len(postData['last_name'])<2:
            errors['last_name']="must have more than 2 characters in last name"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        if 'password_initial' in postData:
            if postData['password_initial']!=postData['password_confirm']:
                errors['password']="passwords must match"
        allUsers=User.objects.all()
        for user in allUsers:
            if postData['email']==user.email:
                errors['emailUnique']="Email is already in use"
        today=datetime.now()
        return errors
    def login_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        return errors
    def edit_validator(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="must have more than 2 characters in first name"
        if len(postData['last_name'])<2:
            errors['last_name']="must have more than 2 characters in last name"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address!"
        return errors
class User(models.Model):
    def __repr__(self):
        return f"< User from User table: id:{self.id}, name= {self.first_name}, {self.last_name}>"
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=90)
    hashword = models.CharField(max_length=90)
    user_level= models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

