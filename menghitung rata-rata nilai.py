# Reyhan Putra Adiyatama
# 065002600008
# Fungsi pada pemograman Python

# Fungsi untuk mengonversi nilai huruf ke peringkat
def nilai_ke_angka(huruf):
    if huruf == "A":
        peringkat = 4.00
    elif huruf == "A-":
        peringkat = 3.75
    elif huruf == "B+":
        peringkat = 3.50
    elif huruf == "B":
        peringkat = 3.00
    elif huruf == "B-":
        peringkat = 2.75
    elif huruf == "C+":
        peringkat = 2.50
    elif huruf == "C":
        peringkat = 2.00
    elif huruf == "C-":
        peringkat = 1.75
    elif huruf == "D":
        peringkat = 1.50
    elif huruf == "E":
        peringkat = 1.25
    else:
        peringkat = None

    return peringkat


# Fungsi untuk merata-ratakan nilai
def hitung_rata_rata():
    total_nilai = 0
    jumlah_data = 0

    while True:
        huruf = input("masukkan nilai: ")

        # Berhenti jika langsung menekan Enter kosong
        if huruf == "":
            break

        angka = nilai_ke_angka(huruf)

        if angka is not None:
            print(f"nilai = {angka}")
            total_nilai += angka
            jumlah_data += 1
        else:
            print("Kategori nilai tidak ditemukan, silakan coba lagi.")

    # Menghitung dan menampilkan rata-rata jika ada data yang diinput
    if jumlah_data > 0:
        rata_rata = total_nilai / jumlah_data
        print(f"rata - rata nya adalah: {rata_rata}")


# Memanggil fungsi program
hitung_rata_rata()
