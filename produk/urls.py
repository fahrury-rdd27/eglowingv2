from django.contrib import admin
from django.urls import path, include
from .views import ProdukList, ProdukDetail

urlpatterns = [
    path('products/', ProdukList.as_view()),
    path('products/<str:pk>/', ProdukDetail.as_view()),
]