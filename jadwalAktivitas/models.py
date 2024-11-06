from django.db import models
from asrama.models import Asrama
from Master.models import Pengawas 


# Create your models here.
class Jadwal_Pengawas (models.Model):
    Nama = models.ForeignKey (Pengawas, on_delete=models.CASCADE)
    Pengawas_di = models.ForeignKey (Asrama, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Nama},{self.Pengawas_di}"

class Kegiatan (models.Model):
    ID_Kegiatan = models.AutoField (primary_key=True)
    Nama_kegiatan = models.CharField (max_length=250)
    Tanggal_pelaksanaan = models.DateField ()

    def __str__(self):
        return str(self.Nama_kegiatan)

