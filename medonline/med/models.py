from django.conf import settings
from django.db import models
from django.utils import timezone


class Specialization(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return self.name


class Publication(models.Model):
    author = models.ForeignKey(Doctor, related_name='publications', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Consultation(models.Model):
    pass