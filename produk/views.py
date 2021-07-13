from .models import Produk
from .serializers import ProdukSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import permission_classes

class ProdukList(generics.ListAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukDetail(generics.RetrieveAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer