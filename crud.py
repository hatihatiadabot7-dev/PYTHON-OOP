data = []

def tambah_data():
    id = int(input("Masukkan ID: "))
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")

    data_baru = {
        "id": id,
        "nama": nama,
        "kelas": kelas
    }

    data.append(data_baru)
    print("✅ Data berhasil ditambahkan\n")


def tampil_data():
    if len(data) == 0:
        print("⚠️ Data masih kosong\n")
    else:
        print("\n=== DATA SISWA ===")
        for d in data:
            print(f"ID    : {d['id']}")
            print(f"Nama  : {d['nama']}")
            print(f"Kelas : {d['kelas']}")
            print("------------------")
        print()


def ubah_data():
    id_cari = int(input("Masukkan ID yang ingin diubah: "))
    for d in data:
        if d["id"] == id_cari:
            d["nama"] = input("Masukkan Nama baru: ")
            d["kelas"] = input("Masukkan Kelas baru: ")
            print("✅ Data berhasil diubah\n")
            return
    print("❌ ID tidak ditemukan\n")


def hapus_data():
    id_cari = int(input("Masukkan ID yang ingin dihapus: "))
    for d in data:
        if d["id"] == id_cari:
            data.remove(d)
            print("✅ Data berhasil dihapus\n")
            return
    print("❌ ID tidak ditemukan\n")


while True:
    print("=== MENU ===")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("👋 Program selesai")
        break
    else:
        print("⚠️ Pilihan tidak valid\n")
