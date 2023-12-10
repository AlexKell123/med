from django.contrib import admin
from .models import Specialization, Doctor, Publication, Consultation

admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Publication)
admin.site.register(Consultation)