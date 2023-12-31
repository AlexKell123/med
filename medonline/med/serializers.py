from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Doctor, Specialization, Publication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']


class DoctorSerializer(serializers.ModelSerializer):
    publications = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'publications']


class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = ['id', 'name']

class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Publication
        fields = ['id', 'author', 'title', 'text', 'date']

