from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Specialization(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.TextField()
    specialization = models.ManyToManyField(Specialization, related_name='doctors')

    def __str__(self):
        return self.name


class Publication(models.Model):
    author = models.ForeignKey(Doctor, related_name='publications', on_delete=models.CASCADE, null=True)
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class WorkTime(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='work_times', on_delete=models.CASCADE)

    class Suit(models.IntegerChoices):
        MON = 0
        TUE = 1
        WED = 2
        THI = 3
        FRI = 4
        SAT = 5
        SUN = 6
    day = models.IntegerField(choices=Suit)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)


class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='consultations', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, related_name='consultations', on_delete=models.CASCADE)


class SpecialWorkTime(models.Model):
    date = models.DateField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)