from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from rest_framework_swagger.views import get_swagger_view


def show_index(request):
    return render(request, 'med/index.html')


schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('med/', include('med.urls')),
]
