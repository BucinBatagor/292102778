from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lapangan/',views.lapangan, name='lapangan'),
    path('booking/',views.booking, name='booking'),
    path('pilih-lapangan/',views.pilih_lapangan, name='pilih_lapangan'),
    path('jadwal/<int:lapangan_id>/',views.detail_jadwal, name='detail_jadwal'),

    path('booking/', views.booking, name='booking'),
    path('booking/tarif/<int:tarif_id>/', views.booking, name='booking_dengan_tarif'),
]
