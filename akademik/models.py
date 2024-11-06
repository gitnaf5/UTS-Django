from django.db import models
from administrasi_santri.models import Santri 
from Master.models import Pengajar
# Create your models here.

class Jadwal_Pelajaran (models.Model):

    PILIH_HARI = [
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jum\'at'),
        ('sabtu', 'Sabtu'),
    ]

    ID_Jadwal = models.AutoField (primary_key=True)
    Hari = models.CharField (max_length=20, choices=PILIH_HARI)
    Nama_pelajaran = models.CharField (max_length=100,null=True)

    def __str__(self):
        return f"{self.Hari}, {self.Nama_pelajaran}"
    
