from django.db import models

class User(models.Model):
    creatingProfileFor = models.CharField(max_length=20)
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    contactNo = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    confirm = models.CharField(max_length=255)
