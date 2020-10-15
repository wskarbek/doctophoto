from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Examination(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)


class ExaminationPhoto(models.Model):
    image = models.CharField(max_length=200)