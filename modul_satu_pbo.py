# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/

# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini

# modul_satu_pbo.py
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama  
        self.nim = nim    
    
    def tampilkan_info(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"

def hitung_luas_persegi(panjang, lebar):
    return panjang * lebar  # Fungsi untuk menghitung luas persegi panjang
