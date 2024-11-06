from django.db import models

# Create your models here.

class Pengajar (models.Model):
    ID_Pengajar = models.AutoField (primary_key=True)
    Nama_pengajar = models.CharField (max_length=100)
    Mata_pelajaran = models.CharField (max_length=100)
    No_telepon_pengajar = models.CharField (max_length=15)

    def __str__(self):
        return f"{self.Nama_pengajar}, {self.Mata_pelajaran}"
    
class Pengawas (models.Model):
    Nama_pengawas = models.CharField (max_length=100)

    def __str__(self) :
        return str(self.Nama_pengawas)
