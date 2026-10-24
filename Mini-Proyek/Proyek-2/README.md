# Student Performance Analyzer

Program sederhana berbasis Python untuk menganalisis nilai siswa menggunakan library **NumPy**. Program ini menyediakan menu interaktif untuk menampilkan nilai, menghitung statistik, mencari siswa dengan performa terbaik, dan menganalisis data nilai yang hilang.

Proyek ini dibuat sebagai latihan untuk memperdalam dasar-dasar Python dan penggunaan NumPy dalam analisis data.

## Fitur Program

Program menyediakan fitur-fitur berikut melalui menu interaktif di terminal:

1. **Melihat Nilai Siswa** — Menampilkan seluruh data nilai siswa.
2. **Melihat Data Nilai Tidak Lengkap** — Menampilkan dataset yang memiliki nilai hilang (`NaN`).
3. **Laporan Nilai Siswa** — Menghitung rata-rata setiap mata pelajaran dan setiap siswa, menampilkan siswa dengan rata-rata minimal 80, serta menampilkan statistik nilai keseluruhan.
4. **Mencari Nilai Tertinggi** — Menampilkan nama siswa, mata pelajaran, dan nilai tertinggi.
5. **Mencari Siswa dengan Rata-rata Tertinggi** — Menentukan siswa yang memiliki rata-rata nilai paling tinggi.
6. **Mencari Siswa Paling Konsisten** — Menentukan siswa dengan standar deviasi nilai paling rendah.
7. **Analisis Mata Pelajaran** — Menghitung rata-rata, nilai maksimum, nilai minimum, dan standar deviasi setiap mata pelajaran.
8. **Analisis Data Hilang** — Menghitung jumlah nilai yang hilang dan tersedia serta menghitung rata-rata dengan mengabaikan nilai yang hilang.
9. **Keluar** — Mengakhiri program.

## Teknologi yang Digunakan

- **Python** — Bahasa pemrograman untuk membangun logika dan alur program.
- **NumPy** — Library untuk pengolahan array dan perhitungan numerik.

## Persyaratan

- Python versi 3.10 atau lebih baru.
- Library NumPy.

Python versi 3.10 atau lebih baru diperlukan karena program menggunakan sintaks `match-case`.

## Cara Menjalankan Program

### 1. Instal NumPy

Buka terminal, kemudian jalankan perintah berikut:

```bash
pip install numpy
```

### 2. Jalankan Program

Simpan kode program dengan nama file `main.py`, kemudian jalankan perintah:

```bash
python main.py
```

### 3. Gunakan Menu

Pilih angka `1` sampai `9` sesuai fitur yang ingin digunakan. Ikuti petunjuk yang ditampilkan di terminal.

## Dataset

Program menggunakan data contoh dari lima siswa:

- Andi
- Budi
- Citra
- Dinda
- Eko

Setiap siswa memiliki nilai dari tiga mata pelajaran:

- Matematika
- Informatika
- Bahasa Inggris

Terdapat dua dataset dalam program:

- **Dataset nilai lengkap**, yang digunakan untuk analisis performa siswa.
- **Dataset latihan dengan nilai hilang**, yang digunakan untuk mempraktikkan analisis data tidak lengkap.

Nilai yang hilang direpresentasikan menggunakan `NaN`. Seluruh nama dan nilai siswa merupakan data contoh untuk keperluan pembelajaran.

## Konsep NumPy yang Dipelajari

- Membuat dan mengolah NumPy array.
- Memahami dimensi array melalui `size`, `shape`, dan `ndim`.
- Menghitung rata-rata dengan `np.mean()` dan `np.nanmean()`.
- Mencari nilai maksimum dan minimum.
- Menggunakan parameter `axis` untuk menghitung statistik berdasarkan baris dan kolom.
- Melakukan penyaringan data menggunakan Boolean masking.
- Mencari indeks dengan `np.argmax()` dan `np.argmin()`.
- Menggunakan `np.unravel_index()` untuk menemukan posisi nilai pada array dua dimensi.
- Menghitung standar deviasi menggunakan `np.std()`.
- Mendeteksi nilai yang hilang menggunakan `np.isnan()`.

## Batasan Proyek

Proyek ini merupakan program analisis nilai tingkat pemula yang dijalankan melalui terminal dengan dataset yang sudah ditentukan di dalam kode.

Saat ini, program belum mendukung penambahan atau pengubahan data siswa melalui menu, penyimpanan data ke file, maupun impor dataset dari sumber eksternal.

## Tujuan Pembelajaran

Proyek ini bertujuan untuk memperkuat pemahaman dasar Python dan memberikan pengalaman praktik menggunakan NumPy untuk analisis data sebagai persiapan mempelajari pengolahan data, Data Science, dan Machine Learning.

---

**Nama Proyek:** Student Performance Analyzer  
**Bahasa Pemrograman:** Python  
**Library Utama:** NumPy