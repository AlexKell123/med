from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.show_all_doctors, name='show_all_doctors'),
    path('doctors/<int:pk>/', views.current_doctor, name='current_doctor'),
    path('specializations', views.show_all_specializations, name='show_all_specializations'),
    path('specializations/<int:pk>/', views.current_specialization, name='current_specialization'),
    path('publication/<int:pk>/', views.current_publication, name='current_publication'),
]