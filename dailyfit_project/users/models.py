# users/models.py
from django.db import models
from django.contrib.auth.models import User
from core.models import ModelBase

class UserProfile(ModelBase):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    years = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username
