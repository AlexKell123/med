from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Doctor, Specialization, Publication, Consultation, WorkTime, SpecialWorkTime


class AllSpecializationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'


class OneSpecializationSerializer(AllSpecializationsSerializer):
    class DoctorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Doctor
            fields = ['id', 'name']
    doctors = DoctorSerializer(many=True)


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = ['day', 'start_time', 'end_time']


class SpecialWorkTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialWorkTime
        fields = ['date', 'start_time', 'end_time']


class AllDoctorsSerializer(serializers.ModelSerializer):
    specialization = AllSpecializationsSerializer(many=True)

    class Meta:
        model = Doctor
        # depth = 1
        fields = '__all__'


class OneDoctorSerializer(AllDoctorsSerializer):
    class PublicationSerializer(serializers.ModelSerializer):

        class Meta:
            model = Publication
            fields = ['id', 'title', 'date']

    publications = PublicationSerializer(many=True)
    # publications = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    work_time = WorkTimeSerializer(many=True)


class PublicationSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Publication
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consultation
        fields = ['id', 'datetime']


class OneConsultationSerializer(serializers.ModelSerializer):
    doctor_name = serializers.ReadOnlyField(source='doctor.name')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return Consultation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.doctor = validated_data.get("doctor", instance.doctor)
        instance.datetime = validated_data.get("datetime", instance.datetime)
        instance.save()
        return instance

    class Meta:
        model = Consultation
        fields = '__all__'
