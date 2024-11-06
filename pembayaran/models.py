from django.db import models

from administrasi_santri.models import Santri

# Create your models here.

class Pembayaran (models.Model):
    METODE_PEMBAYARAN = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
    ]

    Jumlah_pembayaran = models.CharField (null=False)
    Tanggal_pembayaran = models.DateField()
    Metode_pembayaran = models.CharField (max_length=10, choices=METODE_PEMBAYARAN, default="Cash")
    ID_Santri = models.ForeignKey(Santri, on_delete=models.CASCADE)



