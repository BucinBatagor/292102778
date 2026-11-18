from django.shortcuts import render
from .models import Barang


def daftar_barang(request):
    data = Barang.objects.all()
    return render(request, 'barang/daftar_barang.html', {'data': data})
    