from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('doctors/', views.AllDoctorsList.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view()),
    path('specializations/', views.AllSpecializationsList.as_view()),
    path('specializations/<int:pk>/', views.SpecializationDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)