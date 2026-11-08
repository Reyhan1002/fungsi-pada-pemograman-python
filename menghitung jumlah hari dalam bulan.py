# Reyhan Putra Adiyatama
# 065002600008
# Fungsi pada Pemrograman Python

# Fungsi mengecek apakah tahun merupakan kabisat
def cek_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False


# Fungsi menentukan jumlah hari berdasarkan bulan dan tahun
def hitung_hari(bulan, tahun):
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        return 31
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        return 30
    elif bulan == 2:
        if cek_kabisat(tahun):
            return 29
        else:
            return 28
    else:
        return 0


print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

while True:
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))

    # Jika menginputkan 0, program berhenti
    if bulan == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break

    tahun = 0

    # Jika bulan Februari, minta input tahun
    if bulan == 2:
        tahun = int(input("masukkan tahun (e.g., 2021): "))

    # Panggil fungsi hitung_hari
    jumlah_hari = hitung_hari(bulan, tahun)
    print(f"{jumlah_hari} hari dalam sebulan")
