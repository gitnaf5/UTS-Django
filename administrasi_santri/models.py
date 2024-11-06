from django.db import models

# Create your models here.


class OrangTua_Wali (models.Model):
    ID_Ortu_wali = models.AutoField (primary_key=True)
    Nama_wali = models.CharField (max_length=100)
    Hubungan = models.CharField ()
    No_telepon_wali = models.CharField (max_length=15)

    def __str__(self) :
        return f"{self.Nama_wali},{self.No_telepon_wali}"

class Pendaftaran (models.Model):

    STATUS_PENDAFTARAN = [
        ('belum_terdaftar', 'Belum terdaftar'),
        ('terdaftar', 'Sudah Terdaftar'),
    ]

    ID_Pendaftaran = models.AutoField (primary_key=True)
    Tanggal_pendaftaran = models.DateField ()
    Status_pendaftaran = models.CharField (max_length=20, choices=STATUS_PENDAFTARAN, default="Belum terdaftar")
    ID_Ortu_wali = models.ForeignKey (OrangTua_Wali, on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.Status_pendaftaran}, {self.ID_Ortu_wali}"

class Santri (models.Model):
    ID_Santri = models.AutoField (primary_key= True)
    Nama = models.CharField (max_length=100)
    Alamat = models.CharField (max_length=200)
    Tanggal_lahir = models.DateField ()
    No_telepon = models.CharField (max_length=15)
    ID_pendaftaran = models.ForeignKey(Pendaftaran, on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.Nama},{self.ID_Santri}"
    
class Kelas(models.Model):
    PILIH_KELAS = [
        ('iqro', 'Iqro'),
        ('juz amma', 'Juz amma'),
        ('qur\'an', 'Qur\'an')
    ]
    Nama_kelas = models.CharField (max_length=20, choices=PILIH_KELAS)

    def __str__(self):
        return str (self.Nama_kelas)
