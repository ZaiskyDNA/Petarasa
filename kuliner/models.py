from django.db import models

class LokasiKuliner(models.Model):
    AREA_CHOICES = [
        ('KOTA', 'Kota Yogyakarta'),
        ('SLEMAN', 'Sleman'),
        ('BANTUL', 'Bantul'),
        ('KULONPROGO', 'Kulon Progo'),
        ('GUNUNGKIDUL', 'Gunungkidul'),
    ]
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    deskripsi = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_produk_lokal = models.BooleanField(default=False, verbose_name="Label Produk Lokal")
    is_resep_asli = models.BooleanField(default=False, verbose_name="Label Resep Asli")
    foto_utama = models.ImageField(upload_to='lokasi_kuliner/', blank=True, null=True) 
    area = models.CharField(max_length=50, choices=AREA_CHOICES, blank=True)
    jam_buka = models.CharField(max_length=100, blank=True)
    rentang_harga = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nama

class Ulasan(models.Model):
    lokasi = models.ForeignKey(LokasiKuliner, on_delete=models.CASCADE, related_name='ulasan')
    nama_pengulas = models.CharField(max_length=50)
    rating = models.IntegerField(default=1)
    komentar = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ulasan untuk {self.lokasi.nama} oleh {self.nama_pengulas}"

class JalurRasa(models.Model):
    nama_jalur = models.CharField(max_length=100)
    deskripsi = models.TextField()
    lokasi = models.ManyToManyField(LokasiKuliner, related_name='jalur')

    def __str__(self):
        return self.nama_jalur
