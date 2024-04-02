from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter

from .views import DoctorViewSet, SpecializationViewSet, PublicationViewSet, ConsultationViewSet, ConsultationsView



router = DefaultRouter()

# router.register(r'users', UserViewSet, basename='user')
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'specializations', SpecializationViewSet, basename='specializations')
router.register(r'publications', PublicationViewSet, basename='publications')
# router.register(r'work_times', WorkTimeViewSet, basename='work_times')
router.register(r'consultations', ConsultationViewSet, basename='consultations')


urlpatterns = [
    path('consultations/<int:start_year>-<int:start_month>-<int:start_day>/<int:end_year>-<int:end_month>-<int:end_day>'
         '/<int:doctor>', ConsultationsView.as_view()),
]

urlpatterns += router.urls


#TODO не оставлять мусор

# schema_view = get_swagger_view(title='API')

# urlpatterns = [
#     path('s', schema_view),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)