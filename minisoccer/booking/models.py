from django.db import models


class Lapangan(models.Model):
    JENIS_CHOICES = [
        ('sintetis', 'Lapangan Sintetis'),
        ('premium', 'Lapangan Premium'),
    ]

    STATUS_CHOICES = [
        ('tersedia', 'Tersedia'),
        ('maintenance', 'Maintenance'),
        ('tidak_tersedia', 'Tidak Tersedia'),
    ]

    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='lapangan/', blank=True, null=True)
    jenis = models.CharField(
        max_length=20,
        choices=JENIS_CHOICES,
    )
    harga = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='tersedia',
    )
    lokasi = models.CharField(max_length=225)
    ukuran = models.CharField(max_length=50)
    kapasitas = models.CharField(max_length=50)
    deskripsi = models.TextField()
    jam_operasional = models.CharField(max_length=50)

    fasilitas = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Lapangan'
        verbose_name_plural = 'Data Lapangan'
        ordering = ['id']

    def __str__(self):
        return self.nama

    def harga_format(self):
        return f"Rp {self.harga:,.0f}".replace(',', '.')


class Jadwal(models.Model):
    lapangan = models.ForeignKey(
        Lapangan,
        on_delete=models.CASCADE,
    )
    hari = models.CharField(max_length=20)
    jam_buka = models.TimeField()
    jam_tutup = models.TimeField()

    class Meta:
        verbose_name = 'Jadwal'
        verbose_name_plural = 'Data Jadwal'
        ordering = ['id']

    def __str__(self):
        return f'{self.lapangan} - {self.hari}'


class TarifSewa(models.Model):
    JENIS_HARI = [
        ('KERJA', 'Senin - Jumat'),
        ('AKHIR_PEKAN', 'Sabtu - Minggu'),
    ]

    lapangan = models.ForeignKey(
        Lapangan,
        on_delete=models.CASCADE,
    )
    jenis_hari = models.CharField(
        max_length=20,
        choices=JENIS_HARI,
    )
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    harga_per_jam = models.DecimalField(
        max_digits=10,
        decimal_places=0,
    )

    class Meta:
        verbose_name = 'Tarif Sewa'
        verbose_name_plural = 'Data Tarif Sewa'
        ordering = ['id']

    def __str__(self):
        return (
            f'{self.lapangan} - '
            f'{self.get_jenis_hari_display()} '
            f'({self.jam_mulai} - {self.jam_selesai})'
        )

    def harga_format(self):
        return f"Rp {self.harga_per_jam:,.0f}".replace(',', '.')


class Booking(models.Model):
    STATUS_PEMBAYARAN = [
        ('pending', 'Menunggu Pembayaran'),
        ('lunas', 'Lunas / Dikonfirmasi'),
        ('batal', 'Dibatalkan'),
    ]

    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    tarif = models.ForeignKey(TarifSewa, on_delete=models.SET_NULL, null=True, blank=True)
    nama_pemesan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=20)
    tanggal_booking = models.DateField()
    jam_mulai = models.TimeField()
    durasi = models.PositiveIntegerField(default=1, help_text="Durasi dalam jam")
    total_harga = models.DecimalField(max_digits=12, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_PEMBAYARAN, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama_pemesan} - {self.lapangan.nama} ({self.tanggal_booking})"
