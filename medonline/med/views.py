from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Doctor, Specialization, Publication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class AllDoctorsList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class DoctorDetail(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class AllSpecializationsList(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer


class SpecializationDetail(generics.RetrieveAPIView):
    queryset = Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

