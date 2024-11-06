from django.db import models
from administrasi_santri.models import Santri

# Create your models here.

class Asrama (models.Model):

    PILIH_ASRAMA = [
        ('putra', 'Putra'),
        ('putri', 'Putri'),
    ]

    ID_Asrama = models.AutoField (primary_key=True)
    Nama_asrama = models.CharField (max_length=6, choices=PILIH_ASRAMA)
    Jumlah_kamar = models.SmallIntegerField (default=2)

    def __str__(self) :
        return str(self.Nama_asrama)

class Kamar (models.Model):
    ID_Kamar = models.AutoField (primary_key=True)
    Nomor_kamar = models.PositiveIntegerField ()
    Kapasitas = models.PositiveSmallIntegerField (default=2)

    def __str__(self) -> str:
        return f"{self.Nomor_kamar} {self.Kapasitas}"

class Penempatan_Asrama (models.Model):
    ID_Penempatan = models.AutoField (primary_key=True)
    ID_Santri = models.ForeignKey (Santri, on_delete=models.CASCADE)
    ID_Asrama = models.ForeignKey (Asrama, on_delete=models.CASCADE)
    ID_Kamar = models.ForeignKey (Kamar, on_delete=models.CASCADE)


