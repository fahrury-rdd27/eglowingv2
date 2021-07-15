from rest_framework import serializers
from .models import ConsultantProfile, PatientProfile

class ConsultantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantProfile
        fields = ['id', 'first_name', 'last_name', 'alamat_domisili',
        'tanggal_lahir', 'no_rekening', 'pengalaman_praktek', 'izin_praktek', 'ktp']

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'first_name', 'last_name', 'alamat_domisili',
        'tanggal_lahir', 'jenis_kulit']