from django.db import models
import re
from datetime import date, datetime

# Create your models here.
class SignalManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['name'])<2:
            errors['first_name']="must have more than 2 characters in name"
        return errors
class EntranceSignal(models.Model):
    def __repr__(self):
        return f"<Signal from Signal table id:{self.id}, time:{self.timestamp}>"
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=45)
    timestamp = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SignalManager()