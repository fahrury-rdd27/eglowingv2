from django.contrib import admin
from .models import PatientProfile, ConsultantProfile

admin.site.register(PatientProfile)
admin.site.register(ConsultantProfile)
