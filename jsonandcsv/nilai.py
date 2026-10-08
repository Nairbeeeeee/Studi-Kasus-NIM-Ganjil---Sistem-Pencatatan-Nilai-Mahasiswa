import json
import os

def load_data():
    if not os.path.exists("data_nilai.json"):
        with open ("data_nilai.json", "w") as f:
            json.dump([], f)
            return []

    with open("data_nilai.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def simpan_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def tampil_nilai(data):
    print("\n" + "=" * 45)
    print("Riwayat nilai Mahasiswa")
    print("=" * 45)

    if not data :
        print("Belum ada data yang tersimpan")
    else:
        print(f"{'No':<4} | {'NIM':<10} | {'Nama':<15} | {'Nilai':<5}")
        print("=" * 45)
        for i,mhs in enumerate(data, start=1):
            print(f"{i:<4} | {mhs['nim']:<10} | {mhs['nama']:<15} | {mhs['nilai']:<5}")
    print("=" * 45)

def tambah_nilai(data):
    print("\n===Tambah Nilai Baru===")
    nim = input ("Masukkan NIM  :   ")
    nama = input ("Masukkan Nama  :   ")

    while True:
        try:
            nilai = float(input("Masukkan Nilai  : "))
            break
        except ValueError:
            print("Nilai harus berupa angka! Coba Lagi.")

    data_baru = {
        "nim" : nim,
        "nama" : nama,
        "nilai" : nilai
    }

    data.append(data_baru)
    simpan_data(data)
    print(f"\nData Nilai untuk {nama} ({nim}) berhasil disimpan")

def main():
        data_nilai = load_data()

        while True:
            print("\n===SISTEM PENCATATAN NILAI MAHASISWA===")
            print("1. Lihat riwayat nilai")
            print("2. Tambah nilai baru")
            print("3. Keluar")

            pilihan = input("Pilih menu (1-3): ")

            if pilihan == "1":
                tampil_nilai(data_nilai)
            elif pilihan == "2":
                tambah_nilai(data_nilai)
            elif pilihan == "3":
                print("\nTerima Kasih!")
                break
            else:
                print("Pilihan tidak valid!")

main()
