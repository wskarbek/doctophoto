from django.db import models
from django.contrib.auth.models import User


class DoctorTitle(models.Model):
    full = models.CharField(max_length=30)
    short = models.CharField(max_length=10)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.ForeignKey(DoctorTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class Examination(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=350)
    photo = models.ImageField(blank=True, upload_to='scans')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
