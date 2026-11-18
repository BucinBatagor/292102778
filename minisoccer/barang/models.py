from django.db import models


class Barang(models.Model):
    KATEGORI_CHOICES = [
        ('Alat Tulis Kantor', 'Alat Tulis Kantor'),
        ('Mebel', 'Mebel'),
        ('Elektronik', 'Elektronik'),
    ]

    kode_barang = models.CharField('Kode barang', max_length=10, unique=True)
    nama_barang = models.CharField('Nama barang', max_length=100)
    kategori = models.CharField(
        'Kategori',
        max_length=50,
        choices=KATEGORI_CHOICES,
        blank=True,
    )
    stok = models.IntegerField('Stok', default=0)
    harga_beli = models.DecimalField('Harga beli', max_digits=12, decimal_places=2)
    harga_jual = models.DecimalField('Harga jual', max_digits=12, decimal_places=2)
    dibuat_pada = models.DateTimeField('Dibuat pada', auto_now_add=True)
    terakhir_diubah = models.DateTimeField('Terakhir diubah', auto_now=True)

    class Meta:
        verbose_name = 'produk'
        verbose_name_plural = 'produk'
        ordering = ['nama_barang']

    def __str__(self):
        return f'{self.kode_barang} - {self.nama_barang}'
