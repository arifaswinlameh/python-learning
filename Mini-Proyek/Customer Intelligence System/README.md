# Customer Intelligence System

Aplikasi analisis pelanggan berbasis Python dan NumPy yang digunakan untuk mengolah data transaksi, menganalisis perilaku pelanggan, serta menghasilkan insight bisnis melalui menu interaktif di terminal.

## Fitur

- **Dashboard Bisnis** — Menampilkan total pendapatan, jumlah transaksi, total produk terjual, dan statistik pelanggan.
- **Top 10 Pelanggan** — Mengurutkan pelanggan berdasarkan total belanja tertinggi.
- **Filter Pelanggan** — Menampilkan pelanggan yang total belanjanya berada di atas rata-rata.
- **Pencarian Pelanggan** — Mencari pelanggan berdasarkan nama dan menampilkan informasi transaksinya.
- **Analisis Perilaku Pelanggan** — Mengidentifikasi pelanggan dengan jumlah produk terbanyak dan rata-rata belanja per transaksi tertinggi.
- **Insight Otomatis** — Membandingkan jumlah pelanggan yang belanjanya di atas rata-rata dengan pelanggan lainnya.

## Teknologi yang Digunakan

- Python
- NumPy

## Konsep yang Dipelajari

- Pembuatan dan manipulasi array NumPy
- Array dua dimensi dan pengaksesan kolom
- Operasi agregasi dan perhitungan statistik
- Boolean masking dan filtering data
- Pengurutan dan pemeringkatan menggunakan `np.argsort()`
- Pencarian data menggunakan `np.any()` dan `np.argmax()`
- Pemrograman modular menggunakan fungsi
- Menu interaktif dan logika percabangan

## Dataset

Aplikasi menggunakan dataset buatan yang terdiri dari 100 pelanggan.

Setiap data pelanggan memiliki informasi berikut:

| Atribut | Deskripsi |
|---|---|
| Nama pelanggan | Identitas pelanggan |
| Jumlah transaksi | Banyaknya transaksi pelanggan |
| Total belanja | Total pengeluaran pelanggan dalam rupiah |
| Jumlah produk | Total produk yang dibeli pelanggan |

Dataset dibuat secara matematis untuk keperluan pembelajaran dan eksperimen. Data ini bukan berasal dari transaksi pelanggan sungguhan.

## Cara Menjalankan Program

1. Pastikan Python sudah terinstal di komputer.
2. Instal NumPy melalui terminal:

   ```bash
   pip install numpy
   ```

3. Simpan kode program dengan nama `customer_intelligence.py`.
4. Jalankan program menggunakan perintah:

   ```bash
   python customer_intelligence.py
   ```

5. Pilih menu yang tersedia untuk menggunakan fitur aplikasi.

## Tujuan Proyek

Proyek ini dibuat untuk memperkuat pemahaman Python dasar dan mempraktikkan analisis data numerik menggunakan NumPy sebagai persiapan untuk mempelajari Pandas, Data Analysis, dan Machine Learning.

---

**Status:** Selesai

**Jenis Proyek:** Proyek Pembelajaran — Python & NumPy
