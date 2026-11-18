from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Lapangan, Jadwal, TarifSewa, Booking


PILIHAN_FASILITAS = [
    ('Rumput sintesis', 'Rumput sintesis'),
    ('Lampu penerangan', 'Lampu penerangan'),
    ('Ruang ganti', 'Ruang ganti'),
    ('Toilet', 'Toilet'),
    ('Area parkir', 'Area parkir'),
    ('Kantin', 'Kantin'),
]


class LapanganAdminForm(forms.ModelForm):
    fasilitas = forms.MultipleChoiceField(
        choices=PILIHAN_FASILITAS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Fasilitas'
    )

    class Meta:
        model = Lapangan
        fields = '__all__'


@admin.register(Lapangan)
class LapanganAdmin(admin.ModelAdmin):
    form = LapanganAdminForm

    list_display = (
        'id',
        'preview_gambar',
        'nama',
        'jenis',
        'harga',
        'status',
        'lokasi',
        'daftar_fasilitas',
    )

    list_filter = ('jenis', 'status')
    search_fields = ('nama', 'lokasi')

    @admin.display(description='Gambar')
    def preview_gambar(self, obj):
        if obj.gambar:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.gambar.url
            )
        return "-"

    @admin.display(description='Fasilitas')
    def daftar_fasilitas(self, obj):
        return ', '.join(obj.fasilitas or [])


# Admin Jadwal
@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = (
        'lapangan',
        'hari',
        'jam_buka',
        'jam_tutup',
    )

    list_filter = ('hari', 'lapangan')
    ordering = ('lapangan', 'hari')


# Admin Tarif Sewa
@admin.register(TarifSewa)
class TarifSewaAdmin(admin.ModelAdmin):
    list_display = (
        'lapangan',
        'jenis_hari',
        'jam_mulai',
        'jam_selesai',
        'harga_per_jam',
    )

    list_filter = ('jenis_hari', 'lapangan')
    search_fields = ('lapangan__nama',)
    ordering = ('lapangan', 'jenis_hari', 'jam_mulai')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nama_pemesan',
        'no_hp',
        'lapangan',
        'tanggal_booking',
        'jam_mulai',
        'durasi',
        'total_harga_format',
        'status',
    )
    list_filter = ('status', 'tanggal_booking', 'lapangan')
    search_fields = ('nama_pemesan', 'no_hp', 'lapangan__nama')
    list_editable = ('status',)
    date_hierarchy = 'tanggal_booking'
    ordering = ('-tanggal_booking', '-jam_mulai')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Informasi Pemesan', {
            'fields': ('nama_pemesan', 'no_hp')
        }),
        ('Detail Sewa Lapangan', {
            'fields': ('lapangan', 'tarif', 'tanggal_booking', 'jam_mulai', 'durasi')
        }),
        ('Pembayaran & Status', {
            'fields': ('total_harga', 'status', 'created_at')
        }),
    )

    @admin.display(description='Total Harga')
    def total_harga_format(self, obj):
        return f"Rp {obj.total_harga:,.0f}".replace(',', '.')
