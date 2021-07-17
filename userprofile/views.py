from .models import PatientProfile, ConsultantProfile
from .serializers import PatientProfileSerializer, ConsultantProfileSerializer
from .permissions import IsProfileOwner
from rest_framework import generics

class ConsultantDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (IsProfileOwner, )
    queryset = ConsultantProfile.objects.all()
    serializer_class = ConsultantProfileSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (IsProfileOwner, )
    queryset = ConsultantProfile.objects.all()
    serializer_class = ConsultantProfileSerializer