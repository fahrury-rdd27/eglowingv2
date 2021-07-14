from .models import PatientProfile, ConsultantProfile
from .serializers import PatientProfileSerializer, ConsultantProfileSerializer
from rest_framework import generics
from rest_framework import permissions

class ConsultantDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = ConsultantProfile.objects.all()
    serializer_class = ConsultantProfileSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = ConsultantProfile.objects.all()
    serializer_class = ConsultantProfileSerializer