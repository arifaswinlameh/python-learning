mahasiswa = []

def garis():
    print("----------------------------------------------------")

def tampilkan_menu():
    garis()
    print("                    Menu")
    garis()
    print("1. Tambah mahasiswa")
    print("2. Tampilkan Laporan")
    print("3. Tampilkan mahasiswa dengan rata-rata tertinggi")
    print("4. Keluar dari program")

def tambah_data_mhs(mhs):
    sementara = {"nama":None, "nilai":[]}
    sementara["nama"] = input("Masukkan nama : ")
    for i in range(3):
        nilai = int(input(f"Masukkan nilai ke-{i+1} : "))
        sementara["nilai"].append(nilai)
    mhs.append(sementara)

def tampilkan_data_mhs(mhsa):
    garis()
    print("  Nama    | Nilai-1 | Nilai-2 | Nikai-3 | Rata-rata | Status")
    garis()
    for i, mhs in enumerate(mhsa):
        print(f"{i+1}. {mhs["nama"]}   |   {mhs["nilai"][0]}    |    {mhs["nilai"][1]}   |    {mhs["nilai"][2]}   |    {hitung_rata2(mhs)}   | {status_lulus(hitung_rata2(mhs))}")

def hitung_rata2(mhs):
    total = mhs["nilai"][0]+mhs["nilai"][1]+mhs["nilai"][2]
    return round(total/3,2)

def status_lulus(rata2):
    if rata2 >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"

def mencari_rata2_tertinggi(mhs):
    rata2_tertinggi = hitung_rata2(mhs[0])
    nama_mhs_tertinggi = mhs[0]["nama"]
    for data in mhs:
        if hitung_rata2(data) > rata2_tertinggi:
            rata2_tertinggi = hitung_rata2(data)
            nama_mhs_tertinggi = data["nama"]
    return rata2_tertinggi, nama_mhs_tertinggi

while True:
    tampilkan_menu()
    pilih = input("Pilih (1-4) : ")
    match pilih:
        case '1':
            tambah_data_mhs(mahasiswa)
        case '2':
            if mahasiswa:
                tampilkan_data_mhs(mahasiswa)
            else:
                print("belum ada data Mahasiswa!")
        case '3':
            if mahasiswa:
                nilai, nama = mencari_rata2_tertinggi(mahasiswa)
                print(f"Nilai tertinggi : {nilai}")
                print(f"Nama : {nama}")
            else:
                print("Belum ada data Mahasiswa!")
        case '4':
            print("Terima kasih")
            break
        case _:
            print("Ulangi!")
