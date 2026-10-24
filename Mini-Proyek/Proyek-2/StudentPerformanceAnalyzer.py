import numpy as np

nama = np.array(["Andi", "Budi", "Citra", "Dinda", "Eko"])

nilai = np.array([[80, 90, 75],
                 [70, 85, 80],
                 [95, 90, 92],
                 [60, 75, 70],
                 [85, 80, 88]])

nilai_latihan = np.array([[80, 90, 75],
                         [70, np.nan, 80],
                         [95, 90, 92],
                         [np.nan, 75, 70],
                         [85, 80, 88]])

mapel = ["Matematika", "Informatika", "Bahasa Inggris"]

def menu():
    garis()
    print("                  MENU UTAMA")
    garis()
    print("1. Lihat Nilai siswa")
    print("2. Lihat Nilai nan/kurang lengkap")
    print("3. Tampilkan laporan")
    print("4. Lihat nilai tertinggi")
    print("5. Lihat siswa dengan rata-rata tertinggi")
    print("6. Lihat siswa paling konsisten")
    print("7. Analisis Mata Pelajaran")
    print("8. Analisis data nan/kurang lengkap ")
    print("9. Keluar")

def garis():
    print("---------------------------------------------------")

def tampilkan_laporan(nama, nilai, mapel):
    rata2_mapel = np.mean(nilai, axis=0)
    rata2_siswa = np.mean(nilai, axis=1)
    kondisi = rata2_siswa >= 80
    nama_lulus = nama[kondisi]
    garis()
    print("          LAPORAN ANALISIS NILAI SISWA")
    garis()
    print("1. Rata_rata setiap mata pelajaran")
    for i, mpl in enumerate(mapel):
        print(f"{mpl} : {round(rata2_mapel[i], 2)}")
    garis()
    print("2. Rata_rata setiap siswa")
    for i in range(nama.size):
        print(f"{nama[i]}     : {round(rata2_siswa[i], 2)}")
    garis()
    print("3. Siswa dengan rata_rata minimal 80")
    for nama_siswa in nama_lulus:
        print(nama_siswa, end=' ')
    print('\n')
    garis()
    print("4. Statistik Seluruh nilai")
    print(f"Nilai tertinggi         : {np.max(nilai)}")
    print(f"Nilai terendah          : {np.min(nilai)}")
    print(f"Rata-rata seluruh nilai : {round(np.mean(nilai), 2)}\n")
    garis()

def nilai_tertinggi(nama, nilai, mapel):
    index_tertinggi = np.argmax(nilai)
    index_baris, index_kolom = np.unravel_index(index_tertinggi, nilai.shape)
    print("Nilai Tertinggi")
    print(f"Siswa          : {nama[index_baris]}")
    print(f"Mata Pelajaran : {mapel[index_kolom]}")
    print(f"Nilai          : {np.max(nilai)}")

def siswa_rata2_tertinggi(nama, nilai):
    rata2_siswa = np.mean(nilai, axis=1)
    tertinggi = np.max(rata2_siswa)
    index_tertinggi = np.argmax(rata2_siswa)
    print("Siswa dengan Rata-rata Tertinggi")
    print(f"Nama : {nama[index_tertinggi]}") 
    print(f"Rata-rata : {round(tertinggi, 2)}")   

def siswa_paling_konsisten(nama, nilai):
    std = np.std(nilai, axis=1)
    index = np.argmin(std)
    print("Siswa paling Konsisten")
    print(f"Nama            : {nama[index]}")
    print(f"Standar Deviasi : {round(std[index], 2)}")

def analisis_mapel(mapel, nilai):
    rata2_mapel = np.mean(nilai, axis=0)
    maks = np.max(nilai, axis=0)
    minimal = np.min(nilai, axis=0)
    std = np.std(nilai, axis=0)
    print("Analisis Mata Pelajaran")
    for i, mpl in enumerate(mapel):
        print(f"{i+1}. {mpl}")
        print(f"   Rata-rata       : {round(rata2_mapel[i], 2)}")
        print(f"   Maksimal        : {maks[i]}")
        print(f"   Minimal         : {minimal[i]}")
        print(f"   Standar Deviasi : {round(std[i], 2)}")

def analisis_data_hilang(mapel, nilai):
    rata2_mapel = np.nanmean(nilai, axis=0)
    garis()
    print("              Analisis Data Hilang")
    garis()
    print(f"Jumlah nilai hilang     : {np.sum(np.isnan(nilai))}")
    print(f"Jumlah nilai tersedia   : {nilai.size-np.sum(np.isnan(nilai))}")
    print(f"Rata-rata seluruh nilai : {round(np.nanmean(nilai), 2)}")
    print("Rata-rata setiap mapel : ")
    for i, rata in enumerate(rata2_mapel):
        print(f"{i+1}. {mapel[i]} : {round(rata, 2)}")

while True:
    menu()
    pilih = input("Pilih (1-9) : ")
    garis()

    match pilih:
        case '1':
            print(nilai)
            garis()
        case '2':
            print(nilai_latihan)
            garis()
        case '3':
            tampilkan_laporan(nama, nilai, mapel)
        case '4':
            nilai_tertinggi(nama, nilai, mapel)
            garis()
        case '5':
            siswa_rata2_tertinggi(nama, nilai)
            garis()
        case '6':
            siswa_paling_konsisten(nama, nilai)
            garis()
        case '7':
            analisis_mapel(mapel, nilai)
            garis()
        case '8':
            analisis_data_hilang(mapel, nilai_latihan)
            garis()
        case '9':
            garis()
            print("terima kasih")
            garis()
            break
        case _:
            garis()
            print("Ulangi Input!")
            garis()
