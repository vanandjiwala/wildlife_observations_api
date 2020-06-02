from django.db import models
from django.contrib.auth.models import User


class Species(models.Model):
    name = models.CharField(max_length=255)
    sc_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.name


class Observation(models.Model):
    species = models.ForeignKey(Species,on_delete=models.CASCADE)
    observer = models.ForeignKey(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=255,null=False)
    state = models.CharField(max_length=255,null=False)
    location = models.CharField(max_length=255,null=False)
    lat = models.CharField(max_length=255,null=True)
    long = models.CharField(max_length=255,null=True)
    created_on = models.DateTimeField(auto_now_add=True)



