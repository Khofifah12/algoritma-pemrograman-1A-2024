# Fungsi untuk mencari data berdasarkan atribut tertentu
def cari_data(data_karyawan, atribut, nilai):
    hasil_data = []
    for karyawan in data_karyawan:
        if karyawan[atribut].lower() == nilai.lower():
            hasil_data.append(karyawan)
    return hasil_data

# Fungsi untuk menambah data karyawan
def tambah_karyawan():
    data_karyawan = []
    for i in range(5):  # Menambah 5 karyawan
        print(f'Karyawan ke-{i + 1}')
        nip = input('NIP Karyawan: ')
        nama = input('Nama Karyawan: ')
        alamat = input('Alamat Karyawan: ')
        dep = input('Departemen Karyawan: ')
        jabatan = input('Jabatan Karyawan: ')
        
        # Menambahkan karyawan ke dalam list data_karyawan
        data_karyawan.append({
            'NIP': nip,
            'Nama': nama,
            'Alamat': alamat,
            'Departemen': dep,
            'Jabatan': jabatan
        })
    return data_karyawan  # Mengembalikan data_karyawan yang sudah diisi

# Fungsi utama untuk menjalankan aplikasi
def main():
    # Menambahkan data karyawan
    data_karyawan = tambah_karyawan()
    
    # Menanyakan apakah pengguna ingin mencari data karyawan
    cari = input("Apakah anda ingin mencari data karyawan anda (ya/tidak)? ").lower()
    
    if cari == 'ya':
        print("Fitur Pencarian Karyawan:")
        print("1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Alamat")
        print("4. Cari berdasarkan Departemen")
        print("5. Cari berdasarkan Jabatan")
        print("6. Keluar")
        
        pilih = int(input("Pilih fitur pencarian (1-6): "))
        
        # Menentukan atribut pencarian berdasarkan pilihan
        if pilih == 1:
            atribut = 'NIP'
        elif pilih == 2:
            atribut = 'Nama'
        elif pilih == 3:
            atribut = 'Alamat'
        elif pilih == 4:
            atribut = 'Departemen'
        elif pilih == 5:
            atribut = 'Jabatan'
        elif pilih == 6:
            print("Keluar dari program.")
            return
        
        nilai = input(f"Masukkan nilai untuk {atribut}: ")
        hasil = cari_data(data_karyawan, atribut, nilai)
        
        if hasil:
            print("Data yang ditemukan:")
            for karyawan in hasil:
                print(karyawan)
        else:
            print("Tidak ada data yang cocok.")

# Menjalankan program utama
if __name__ == '__main__':
    main()