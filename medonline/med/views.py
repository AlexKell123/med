from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import re_path

from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer, DoctorSerializer, SpecializationSerializer, PublicationSerializer, \
    WorkTimeSerializer, ConsultationSerializer
from .models import Doctor, Specialization, Publication, WorkTime, Consultation


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class DoctorViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Doctor.objects.all()
        serializer = DoctorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Doctor.objects.all()
        doctor = get_object_or_404(queryset, pk=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)


class SpecializationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Specialization.objects.all()
        serializer = SpecializationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Specialization.objects.all()
        specialization = get_object_or_404(queryset, pk=pk)
        serializer = SpecializationSerializer(specialization)
        return Response(serializer.data)


class PublicationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Publication.objects.all()
        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Publication.objects.all()
        publication = get_object_or_404(queryset, pk=pk)
        serializer = PublicationSerializer(publication)
        return Response(serializer.data)


class WorkTimeViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = WorkTime.objects.all()
        serializer = WorkTimeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = WorkTime.objects.all()
        work_time = get_object_or_404(queryset, pk=pk)
        serializer = WorkTimeSerializer(work_time)
        return Response(serializer.data)


class ConsultationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Consultation.objects.all()
        serializer = ConsultationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Consultation.objects.all()
        consultation = get_object_or_404(queryset, pk=pk)
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data)

    def create(self, request):
        serializer = ConsultationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'consultation': serializer.data})

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Consultation.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ConsultationSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            Consultation.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "deleted consultation " + str(pk)})


# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class AllDoctorsList(generics.ListAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#
#
# class DoctorDetail(generics.RetrieveAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer


# class AllSpecializationsList(generics.ListAPIView):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer
#
#
# class SpecializationDetail(generics.RetrieveAPIView):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer

# class AllPublicationsList(generics.ListAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
#
#
# class PublicationDetail(generics.RetrieveAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer