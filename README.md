# 292102778 — Pemrograman Berbasis Open Source

Tugas mata kuliah Pemrograman Berbasis Open Source (Semester 3, STMIK).

| Folder | Isi |
|---|---|
| `minisoccer/` | Sistem Informasi Penyewaan Lapangan Mini Soccer (app `booking`) + latihan UTS (app `barang`) |
| `laundry/` | Latihan awal Django (app `paket`) |

## Cara menjalankan di komputer lain

1. Clone repo dan masuk ke foldernya

   ```bash
   git clone https://github.com/BucinBatagor/292102778.git
   cd 292102778
   ```

2. Buat virtual environment dan install library

   ```bash
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Siapkan database MariaDB/MySQL bernama `minisoccer_c3`
   (user `root`, password kosong, port `3306` — sesuaikan di `minisoccer/minisoccer/settings.py` bila berbeda).

4. Buat tabel, isi data awal, dan buat akun admin

   ```bash
   cd minisoccer
   py manage.py migrate
   py manage.py loaddata data_awal.json
   py manage.py createsuperuser
   ```

5. Jalankan server lalu buka http://127.0.0.1:8000/

   ```bash
   py manage.py runserver
   ```

`data_awal.json` berisi 3 lapangan, 21 jadwal, 36 tarif sewa, dan 6 data barang.
Foto lapangan ada di `minisoccer/media/lapangan/` (sumber: Wikimedia Commons, lisensi CC BY-SA / CC0).
