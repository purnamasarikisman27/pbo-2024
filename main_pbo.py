# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")


# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py

#main_pbo.py
from modul_satu_pbo import Mahasiswa, hitung_luas_persegi  # Mengimpor Mahasiswa dan hitung_luas_persegi

if __name__ == "__main__":
    # Uji class Mahasiswa
    mhs = Mahasiswa("purnama sari ", "23075")
    print(mhs.tampilkan_info())  # Menampilkan informasi mahasiswa

    # Uji fungsi hitung_luas_persegi
    panjang = 5
    lebar = 3
    Luas_Persegi_Panjang = hitung_luas_persegi(panjang, lebar)  # Menggunakan fungsi untuk menghitung luas
    print(f"Luas Persegi Panjang: {Luas_Persegi_Panjang}")  # Menampilkan hasil luas
