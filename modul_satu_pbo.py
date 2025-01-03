class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = []  
        
    def tampilkan_info(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"
    
    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai.append({"mata_kuliah": mata_kuliah, "nilai": nilai})
    
    def hitung_rata_rata(self):
        if not self.nilai:
            return 0
        total = sum([item["nilai"] for item in self.nilai])
        return total / len(self.nilai)
    
    def ubah_nama(self, nama_baru):
        self.nama = nama_baru
        print(f"Nama berhasil diubah menjadi {self.nama}")
    
    def ubah_nim(self, nim_baru):
        self.nim = nim_baru
        print(f"NIM berhasil diubah menjadi {self.nim}")

    def hitung_luas_persegi(panjang, lebar):
        return panjang * lebar 

    def hitung_luas_segitiga(alas, tinggi):
        return (alas * tinggi) / 2  

 

 
