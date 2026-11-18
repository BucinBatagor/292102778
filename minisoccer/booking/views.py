from django.shortcuts import render, get_object_or_404, redirect
from .models import Lapangan, Jadwal, TarifSewa, Booking
from django.contrib import messages


def home(request):
    return render(request, 'booking/home.html')


def booking(request, tarif_id=None):
    tarif_terpilih = None
    lapangan_terpilih = None
    if tarif_id:
        tarif_terpilih = get_object_or_404(TarifSewa, id=tarif_id)
        lapangan_terpilih = tarif_terpilih.lapangan

    lapangan_list = Lapangan.objects.filter(status='tersedia')
    if request.method == 'POST':
        lapangan_id = request.POST.get('lapangan_id')
        nama_pemesan = request.POST.get('nama_pemesan')
        no_hp = request.POST.get('no_hp')
        tanggal_booking = request.POST.get('tanggal_booking')
        jam_mulai = request.POST.get('jam_mulai')
        durasi = int(request.POST.get('durasi', 1))

        lapangan_obj = get_object_or_404(Lapangan, id=lapangan_id)

        harga_satuan = tarif_terpilih.harga_per_jam if tarif_terpilih else lapangan_obj.harga
        total_harga = harga_satuan * durasi

        Booking.objects.create(
            lapangan=lapangan_obj,
            tarif=tarif_terpilih,
            nama_pemesan=nama_pemesan,
            no_hp=no_hp,
            tanggal_booking=tanggal_booking,
            jam_mulai=jam_mulai,
            durasi=durasi,
            total_harga=total_harga,
        )

        messages.success(request, f'Booking untuk {lapangan_obj.nama} berhasil dibuat!')
        return redirect('booking')

    context = {
        'lapangan_list': lapangan_list,
        'tarif_terpilih': tarif_terpilih,
        'lapangan_terpilih': lapangan_terpilih,
    }
    return render(request, 'booking/booking.html', context)


def lapangan(request):
    lapangan_list = Lapangan.objects.all()

    context = {
        'lapangan': lapangan_list,
    }

    return render(request, 'booking/lapangan.html', context)


def pilih_lapangan(request):
    lapangan_list = Lapangan.objects.all()

    context = {
        'lapangan_list': lapangan_list,
    }

    return render(
        request,
        'booking/pilih_lapangan.html',
        context,
    )


def detail_jadwal(request, lapangan_id):
    lapangan = get_object_or_404(
        Lapangan,
        id=lapangan_id,
    )

    jadwal_list = Jadwal.objects.filter(
        lapangan=lapangan,
    )

    tarif_list = TarifSewa.objects.filter(
        lapangan=lapangan,
    )

    context = {
        'lapangan': lapangan,
        'jadwal_list': jadwal_list,
        'tarif_list': tarif_list,
    }

    return render(
        request,
        'booking/jadwal.html',
        context,
    )
