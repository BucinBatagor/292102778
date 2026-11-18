from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_barang, name='daftar_barang'),
]
