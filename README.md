# Modul Pemesanan Ruangan

Modul Odoo ini dirancang untuk mengelola pemesanan ruangan secara efektif, mencakup pengaturan master ruangan dan pemesanan ruangan dengan validasi yang memastikan tidak ada konflik dalam pemesanan ruangan.

## Fitur
1. **Master Ruangan**:
   - Menyimpan informasi tentang ruangan, seperti nama ruangan, tipe ruangan, lokasi, kapasitas, dan foto.
   - Validasi untuk memastikan nama ruangan unik.

2. **Pemesanan Ruangan**:
   - Menyimpan informasi pemesanan ruangan, termasuk nomor pemesanan otomatis, nama pemesan, tanggal, status pemesanan, dan catatan.
   - Tombol untuk memproses pemesanan dari status **Draft** ke **On Going** hingga **Done**.
   - Validasi untuk memastikan tidak ada pemesanan ruangan dan tanggal yang sama.

## Instalasi

1. **Clone repository ini ke dalam folder `addons` Odoo Anda**:
    ```bash
    git clone https://github.com/jehuakusumadewa/Project-Odoo.git
    ```

2. **Update list modul Odoo**:
    - Masuk ke `Apps` dalam Odoo, dan klik **Update Apps List** untuk memperbarui daftar modul.

3. **Install Modul**:
    - Cari modul `Pemesanan Ruangan` di halaman Apps, kemudian klik **Install**.

## Penggunaan

1. **Master Ruangan**:
   - Navigasi ke menu `Master Ruangan` untuk melihat daftar ruangan yang tersedia.
   - Anda dapat menambahkan ruangan baru dengan mengisi nama, tipe, lokasi, foto, kapasitas, dan deskripsi jika diperlukan.

2. **Pemesanan Ruangan**:
   - Navigasi ke menu `Pemesanan Ruangan` untuk membuat pemesanan baru.
   - Isi nama pemesanan, pilih ruangan yang ingin dipesan, dan tentukan tanggal pemesanan.
   - Simpan pemesanan, kemudian proses pemesanan dengan mengubah status menjadi **On Going** atau **Done** sesuai kebutuhan.

## Validasi

- **Nama Pemesanan**: Harus unik, tidak boleh sama dengan pemesanan yang sudah ada.
- **Nama Ruangan**: Setiap nama ruangan harus unik.
- **Ruangan dan Tanggal Pemesanan**: Tidak boleh ada pemesanan dengan ruangan dan tanggal yang sama.

## Pengembang

- **Nama Pengembang**: Jehua Kusuma Dewa
- **Email**: docjehua22@gmai.com

## Lisensi

Modul ini berlisensi [MIT License](LICENSE).

