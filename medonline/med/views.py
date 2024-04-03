import datetime
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .serializers import AllDoctorsSerializer, OneDoctorSerializer, AllSpecializationsSerializer, \
    OneSpecializationSerializer, PublicationSerializer, ConsultationSerializer, SpecialWorkTimeSerializer, \
    WorkTimeSerializer, OneConsultationSerializer
from .models import Doctor, Specialization, Publication, WorkTime, Consultation, SpecialWorkTime


class SpecializationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Specialization.objects.all()
        serializer = AllSpecializationsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Specialization.objects.all()
        specialization = get_object_or_404(queryset, pk=pk)
        serializer = OneSpecializationSerializer(specialization)
        return Response(serializer.data)


class DoctorViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Doctor.objects.all()
        serializer = AllDoctorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Doctor.objects.all()
        doctor = get_object_or_404(queryset, pk=pk)
        serializer = OneDoctorSerializer(doctor)
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


class ConsultationView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Consultation.objects.filter(doctor=self.kwargs['doctor'],
                                               datetime__range=[datetime.date(self.kwargs['start_year'],
                                                                              self.kwargs['start_month'],
                                                                              self.kwargs['start_day']),
                                                                datetime.date(self.kwargs['end_year'],
                                                                              self.kwargs['end_month'],
                                                                              self.kwargs['end_day'])])

        serializer = ConsultationSerializer(queryset, many=True)
        consultations = serializer.data

        queryset = SpecialWorkTime.objects.filter(doctor=self.kwargs['doctor'],
                                                  date__range=[datetime.date(self.kwargs['start_year'],
                                                                             self.kwargs['start_month'],
                                                                             self.kwargs['start_day']),
                                                               datetime.date(self.kwargs['end_year'],
                                                                             self.kwargs['end_month'],
                                                                             self.kwargs['end_day'])])
        serializer = SpecialWorkTimeSerializer(queryset, many=True)
        special_work_time = serializer.data

        queryset = WorkTime.objects.filter(doctor=self.kwargs['doctor'])
        serializer = WorkTimeSerializer(queryset, many=True)
        work_time = serializer.data

        return Response({'doctor': self.kwargs['doctor'], 'consultations': consultations,
                         'special_work_time': special_work_time, 'work_time': work_time})


class ConsultationViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    # def list(self, request):
    #     queryset = Consultation.objects.all()
    #     serializer = ConsultationSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Consultation.objects.all()
        consultation = get_object_or_404(queryset, pk=pk)
        serializer = OneConsultationSerializer(consultation)
        return Response(serializer.data)

    def create(self, request):
        serializer = OneConsultationSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['datetime'].minute != 0 or serializer.validated_data['datetime'].second != 0:
            return Response({'Incorrect time': serializer.validated_data['datetime'].time()})

        queryset = Consultation.objects.filter(doctor=serializer.validated_data['doctor'],
                                               datetime=serializer.validated_data['datetime'])
        if queryset:
            serializer = ConsultationSerializer(queryset, many=True)
            return Response({'Consultation exist': serializer.data})

        queryset = SpecialWorkTime.objects.filter(doctor=serializer.validated_data['doctor'],
                                                  date=serializer.validated_data['datetime'].date())
        if queryset:
            for i in queryset:
                if i.start_time <= serializer.validated_data['datetime'].time() < i.end_time:
                    serializer.save()
                    return Response({'Consultation created': serializer.data})
            return Response({'No special worktime': serializer.validated_data['datetime'].time() })
        else:
            queryset = WorkTime.objects.filter(doctor=serializer.validated_data['doctor'],
                                               day=serializer.validated_data['datetime'].date().weekday())
            if queryset:
                for i in queryset:
                    if i.start_time <= serializer.validated_data['datetime'].time() < i.end_time:
                        serializer.save()
                        return Response({'Consultation created': serializer.data})
                return Response({'No worktime': serializer.validated_data['datetime'].time()})

            else:
                return Response({'No work today': serializer.validated_data['datetime'].date().weekday()})

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Consultation.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = OneConsultationSerializer(data=request.data, instance=instance, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Consultation updated": serializer.data})

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            Consultation.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"Consultation deleted": str(pk)})




# class UserViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


