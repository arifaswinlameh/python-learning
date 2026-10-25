import numpy as np

nama = np.array([
    "Andi", "Budi", "Citra", "Dinda", "Eko",
    "Fajar", "Gita", "Hendra", "Intan", "Joko",
    "Karin", "Lutfi", "Maya", "Nanda", "Oscar",
    "Putri", "Qori", "Raka", "Sinta", "Tono",
    "Umar", "Vina", "Wahyu", "Xena", "Yusuf",
    "Zahra", "Aditya", "Bella", "Candra", "Dewi",
    "Evan", "Farah", "Galih", "Hana", "Ilham",
    "Jihan", "Kevin", "Laras", "Malik", "Nia",
    "Oki", "Prita", "Rian", "Salma", "Tegar",
    "Ulfa", "Vito", "Wulan", "Yoga", "Zaki",
    "Alya", "Bagas", "Cindy", "Damar", "Elsa",
    "Fikri", "Grace", "Hasan", "Indra", "Jessica",
    "Kiki", "Laila", "Miko", "Nadia", "Omar",
    "Pandu", "Rani", "Surya", "Tiara", "Usman",
    "Vera", "Wildan", "Xavier", "Yuni", "Zidan",
    "Amira", "Bima", "Clara", "Daffa", "Erika",
    "Fauzan", "Ghani", "Helmi", "Irene", "Jefri",
    "Kezia", "Leo", "Mira", "Niko", "Olivia",
    "Prana", "Raisa", "Sandi", "Tania", "Udin",
    "Vania", "Wijaya", "Yanto", "Zahira", "Adit"
])

# Urutan kolom:
# 0 = jumlah transaksi
# 1 = total belanja (rupiah)
# 2 = jumlah produk dibeli

indeks = np.arange(100)

transaksi = (indeks * 7 + 3) % 20 + 1
total_belanja = transaksi * ((indeks * 1379 + 25000) % 175000 + 25000)
jumlah_produk = (transaksi * 3 + indeks * 2) % 45 + 1

data = np.stack((transaksi, total_belanja, jumlah_produk), axis=1)

def garis():
    print("====================================")

def garis1():
    print("------------------------------------")

def total_pendapatan(data):
    return np.sum(data[:, 1])

def total_transaksi_def(data):
    return np.sum(data[:, 0])

def total_produk_terjual(data):
    return np.sum(data[:, 2])

def pelanggan_maxtransaksi(data):
    return np.max(data[:, 0])

def pelanggan_maxbelanja(data):
    return np.max(data[:, 1])

def pelanggan_minbelanja(data):
    return np.min(data[:, 1])

def rata2_jml_produk(data):
    return np.mean(data[:, 2])

def nama_belanja_tertinggi(nama, data):
    index = np.argmax(data[:, 1])
    return nama[index]

def nama_transaksi_terbanyak(nama, data):
    index = np.argmax(data[:, 0])
    return nama[index]

def nama_belanja_terendah(nama, data):
    index = np.argmin(data[:, 1])
    return nama[index]

def rata_rata_belanja_pelanggan(data):
    return (data[:, 1]/data[:, 0])

def rata_rata_total_belanja(data):
    return total_pendapatan(data)/data.shape[0]

def pelanggan_belanja_diatas_rata_rata(nama, data):
    return nama[data[:, 1] > rata_rata_total_belanja(data)], data[(data[:, 1] > rata_rata_total_belanja(data)), 1]

def ranking_pelanggan(nama, data):
    index_urut = np.argsort(-data[:, 1])
    return nama[index_urut], data[:, 1][index_urut]

def top_10_pelanggan(nama, data):
    nama, belanja = ranking_pelanggan(nama, data)
    for i in range(10):
        print(f"Top {i+1} : {nama[i]} ({belanja[i]})")

def cari_pelanggan(nama, data):
    garis()
    print("        CARI PELANGGAN")
    garis()
    nama_dicari = input("Input nama dicari : ")
    mask = nama == nama_dicari

    if np.any(mask):
        index = np.argmax(mask)
        garis1()
        print("Pelanggan ditemukan!")
        garis1()
        print(f"Nama             : {nama[index]}")
        print(f"Jumlah transaksi : {data[index, 0]}")
        print(f"Total belanja    : Rp{data[index, 1]}")
        print(f"Produk dibeli    : {data[index, 2]}")
        garis()
    else:
        garis1()
        print("Nama tidak ditemukan/tidak ada di database")
        garis()
        


def tampilkan_dashboard(data):
    garis()
    print("             DASHBOARD")
    garis()
    print(f"Jumlah Pelanggan : {data.shape[0]}")
    print(f"Total Pendapatan : Rp{round(total_pendapatan(data), 3)}")
    print(f"Total Transaksi  : {total_transaksi_def(data)}")
    garis1()
    print(f"Total Produk terjual     : {total_produk_terjual(data)}")
    print(f"Rata-rata Transaksi      : {round((total_transaksi_def(data)/data.shape[0]), 3)} / pelanggan")
    print(f"Rata-rata Belanja        : Rp{round((total_pendapatan(data)/data.shape[0]), 3)} / pelanggan")
    print(f"Rata-rata Produk Terjual : {round((total_produk_terjual(data)/data.shape[0]), 3)} / pelanggan")
    garis1()
    print(f"Transaksi terbanyak : {pelanggan_maxtransaksi(data)}")
    print(f"               Nama : {nama_transaksi_terbanyak(nama, data)}")
    print(f"Belanja terbanyak   : Rp{pelanggan_maxbelanja(data)}")
    print(f"               Nama : {nama_belanja_tertinggi(nama, data)}")
    print(f"Belanja tersedikit  : Rp{pelanggan_minbelanja(data)}")
    print(f"               Nama : {nama_belanja_terendah(nama, data)}")
    garis()

def tampilkan_menu(data):
    garis()
    print("   CUSTOMER INTELLIGENCE SYSTEM")
    garis()
    print(f"Total Pelanggan       : {data.shape[0]}")
    print(f"Total Pendapatan      : Rp{round(total_pendapatan(data), 3)}")
    print(f"Rata-rata belanja     : RP{round((total_pendapatan(data)/data.shape[0]), 3)} / pelanggan\n")

    print("1. Lihat Top 10 Pelanggan")
    print("2. Cari Pelanggan di Atas Rata-rata")
    print("3. Lihat Statistik Bisnis")
    print("4. Cari Pelanggan")
    print("5. Analisis Perilaku Pelanggan")
    print("6. Insight Pelanggan")
    print("7. Keluar")
    garis()

def nama_produk_terbanyak(nama, data):
    index = np.argmax(data[:, 2])
    return data[index, 2], nama[index]

def nama_rata2_belanja_tertinggi(nama, data):
    temp = rata_rata_belanja_pelanggan(data)
    index = np.argmax(temp)
    return temp[index], nama[index]

def menu_analisis_perilaku(nama, data):
    produk_terbanyak = nama_produk_terbanyak(nama, data)
    rata2_belanja_tertinggi = nama_rata2_belanja_tertinggi(nama, data)
    print("      Hasil Analisis")
    garis1()
    print("1. Pelanggan dengan produk terbanyak")
    print(f"Nama         : {produk_terbanyak[1]}")
    print(f"Total produk : {produk_terbanyak[0]}")
    garis1()
    print("2. Pelanggan dengan Rata-rata belanja/transaksi tertinggi")
    print(f"Nama              : {rata2_belanja_tertinggi[1]}")
    print(f"Rata-rata belanja : Rp{rata2_belanja_tertinggi[0]}")

def insight_pelanggan(nama, data):
    temp, sem = pelanggan_belanja_diatas_rata_rata(nama, data)
    jumlah_di_atas_rata2 = temp.size
    jumlah_lainnya = nama.size-jumlah_di_atas_rata2
    garis()
    print("INSIGHT PELANGGAN")
    garis1()
    print(f"Pelanggan di atas rata-rata : {jumlah_di_atas_rata2}")
    print(f"Pelanggan lainnya           : {jumlah_lainnya}")
    garis1()
    if jumlah_di_atas_rata2 > jumlah_lainnya:
        print("Mayoritas pelanggan berbelanja di atas rata-rata.")
    elif jumlah_di_atas_rata2 < jumlah_lainnya:
        print("Mayoritas pelanggan berbelanja tidak di atas rata-rata.")
    else:
        print("Jumlah pelanggan terbagi seimbang.")

while True:
    tampilkan_menu(data)
    pilih = input("Pilih menu (1-7) : ")
    garis()
    if pilih == '1':
        print("      TOP 10 PELANGGAN\n  berdasarkan total belanja")
        garis()
        top_10_pelanggan(nama, data)
    elif pilih == '2':
        print("             LIST\npelanggan di atas rata-rata(belanja)")
        garis()
        nama_di_atas_rata2, t_belanja = pelanggan_belanja_diatas_rata_rata(nama, data)
        for i in range(nama_di_atas_rata2.size):
            print(f"{i+1}. {nama_di_atas_rata2[i]} ({t_belanja[i]})")
        garis()
    elif pilih == '3':
        tampilkan_dashboard(data)
    elif pilih == '4':
        cari_pelanggan(nama, data)
        garis()
    elif pilih == '5':
        menu_analisis_perilaku(nama, data)
        garis()
    elif pilih == '6':
        insight_pelanggan(nama, data)
        garis()
    elif pilih == '7':
        garis()
        print("     TERIMA KASIH.....")
        garis()
        break
    else:
        garis()
        print("          ULANGI INPUT!")