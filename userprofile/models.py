from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    alamat_domisili = models.CharField(blank=False, max_length=100)
    tanggal_lahir = models.DateField()

    class Meta:
        abstract = True

class PatientProfile(UserProfile):
    JENIS_KULIT = [
        ('Kering', 'Kering'),
        ('Berminyak', 'Berminyak'),
        ('Normal', 'Normal'),
        ('Sensitif', 'Sensitif'),
    ]
    jenis_kulit = models.CharField(choices=JENIS_KULIT, max_length=30, default='Kering')

    def __str__(self):
        return self.first_name

class ConsultantProfile(UserProfile):
    no_rekening = models.CharField(unique=True, blank=False, max_length=20)
    pengalaman_praktek = models.IntegerField(default=0)
    izin_praktek = models.ImageField(upload_to='images/izin/', blank=True)
    ktp = models.ImageField(upload_to='images/ktp/', blank=True)


    def __str__(self):
        return self.first_name