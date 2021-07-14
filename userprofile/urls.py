from django.urls import path
from .views import ConsultantDetail, PatientDetail

urlpatterns = [
    path('consultant/<str:pk>', ConsultantDetail.as_view()),
    path('patient/<str:pk>/', PatientDetail.as_view()),
]