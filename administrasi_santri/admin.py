from django.contrib import admin

from administrasi_santri.models import * 
from akademik.models import Jadwal_Pelajaran
from asrama.models import *
from jadwalAktivitas.models import *
from pembayaran.models import Pembayaran
from Master.models import *
# Register your models here.

class OrangTuaWaliAdmin(admin.ModelAdmin):
    list_display = ["ID_Ortu_wali", "Nama_wali", "Hubungan", "No_telepon_wali"]

class santriAdmin (admin.ModelAdmin):
    list_display = ["Nama", "No_telepon"]

class jadwalpelajaranAdmin (admin.ModelAdmin):
    list_display = ["Nama_pelajaran", "Hari"]

class penempatanAdmin (admin.ModelAdmin):
    list_display = ["ID_Santri","ID_Asrama","ID_Kamar"]

class jadwalpengawasAdmin (admin.ModelAdmin):
    list_display = ["Nama", "Pengawas_di"]

class kegiatanAdmin (admin.ModelAdmin):
    list_display = ["Nama_kegiatan","Tanggal_pelaksanaan"]

class pembayaranAdmin (admin.ModelAdmin):
    list_display = ["ID_Santri", "Tanggal_pembayaran"]


admin.site.register(OrangTua_Wali, OrangTuaWaliAdmin)
admin.site.register(Pendaftaran)
admin.site.register(Santri,santriAdmin)

admin.site.register(Pengajar)
admin.site.register(Pengawas)

admin.site.register(Jadwal_Pelajaran, jadwalpelajaranAdmin)
#
admin.site.register(Asrama)
admin.site.register(Kamar)
admin.site.register(Penempatan_Asrama, penempatanAdmin)

admin.site.register(Jadwal_Pengawas, jadwalpengawasAdmin)
admin.site.register(Kegiatan, kegiatanAdmin)

admin.site.register(Pembayaran, pembayaranAdmin)


