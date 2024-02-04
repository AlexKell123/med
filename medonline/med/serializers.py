from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Doctor, Specialization, Publication, WorkTime, Consultation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class DoctorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Doctor
            fields = ['id', 'name']
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Specialization
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField()
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Publication
        fields = ['id', 'title', 'text', 'date', 'author_id', 'author_name']


class WorkTimeSerializer(serializers.ModelSerializer):
    doctor_id = serializers.ReadOnlyField()
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = WorkTime
        fields = ['day', 'start_time', 'end_time', 'doctor_id', 'doctor_name']


class ConsultationSerializer(serializers.ModelSerializer):
    doctor_id = serializers.ReadOnlyField()
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = Consultation
        fields = ['datetime', 'doctor_id', 'doctor_name']


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(many=True)
    publications = PublicationSerializer(many=True)
    # publications = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    work_times = WorkTimeSerializer(many=True)
    consultations = ConsultationSerializer(many=True)

    class Meta:
        model = Doctor
        # depth = 1
        fields = ['id', 'name', 'specialization', 'publications', 'work_times', 'consultations']





