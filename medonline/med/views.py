from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Doctor, Specialization, Publication
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def show_all_doctors(request):
    doctors = Doctor.objects.order_by('name')
    return render(request, 'med/all_doctors.html', {'doctors': doctors, 'title': 'Все доктора'})


def show_all_specializations(request):
    specializations = Specialization.objects.order_by('name')
    return render(request, 'med/all_specializations.html', {'specializations': specializations, 'title': 'Все специализации'})


def current_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    publications = Publication.objects.filter(author=pk)
    return render(request, 'med/current_doctor.html', {'doctor': doctor, 'publications': publications})


def current_specialization(request, pk):
    doctors = Doctor.objects.filter(specialization=pk)
    title = 'Доктора со специализацией: ' + get_object_or_404(Specialization, pk=pk).name
    return render(request, 'med/all_doctors.html', {'doctors': doctors, 'title': title})


def current_publication(request, pk):
    pass











