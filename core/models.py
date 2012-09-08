from django.db import models
from django.contrib.admin.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField()
