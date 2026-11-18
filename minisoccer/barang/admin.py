from django.contrib import admin
from .models import Barang


@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    list_display = (
        'kode_barang',
        'nama_barang',
        'kategori',
        'stok',
        'harga_beli',
        'harga_jual',
    )

    list_filter = ('kategori',)
    search_fields = ('kode_barang', 'nama_barang')
    readonly_fields = ('dibuat_pada', 'terakhir_diubah')

    fields = (
        'kode_barang',
        'nama_barang',
        'kategori',
        'stok',
        'harga_beli',
        'harga_jual',
        'dibuat_pada',
        'terakhir_diubah',
    )
