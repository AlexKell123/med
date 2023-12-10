from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def show_index(request):
    return render(request, 'med/index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    path('med/', include('med.urls')),
]
