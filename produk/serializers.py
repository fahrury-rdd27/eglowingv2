from rest_framework import serializers
from .models import Produk

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ['upc', 'nama_produk', 'jenis_produk', 'kandungan', 'manfaat', 'kelebihan', 'kekurangan']