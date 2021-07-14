from .models import Produk
from .serializers import ProdukSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProdukList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer