from django.db import models
from django.contrib.postgres.fields import ArrayField

JENIS_PRODUK = [
    ('Make Up', 'Make Up'),
    ('Skincare', 'Skincare'),
    ('Bodycare', 'Bodycare'),
    ('Vitamin', 'Vitamin'),    
    ('Obat', 'Obat'),
]

class Produk(models.Model):
    upc = models.CharField(max_length=100, unique=True, primary_key=True) # universal product identifier
    nama_produk = models.CharField(max_length=100)
    jenis_produk = models.CharField(choices=JENIS_PRODUK, max_length=30, default='Make Up')
    kandungan = ArrayField(models.CharField(max_length=50), blank=True, null=False)
    manfaat = models.TextField(max_length=300, blank=True)
    kelebihan = models.TextField(max_length=300, blank=True)
    kekurangan = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.nama_produk