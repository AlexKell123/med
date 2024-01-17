from django.contrib import admin
from .models import Specialization, Doctor, Publication, Consultation, WorkTime

admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Publication)
admin.site.register(Consultation)
admin.site.register(WorkTime)