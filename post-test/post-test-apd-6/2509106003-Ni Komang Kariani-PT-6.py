import os

# Membersihkan Terminal Dulu Ya
os.system("cls" if os.name == "nt" else "clear")

# Salam Pembuka dan Sapaan
print("|===============================================================|")
print("|       SELAMAT DATANG DI TOKO PERLENGKAPAN OLAHRAGA            |")
print("|===============================================================|")
print("Halo! Siap berburu perlengkapan olahraga favoritmu?")
print("Kami punya semua yang kamu butuhkan loh.\n")

input("Tekan Enter untuk lanjut ke menu utama..")

# Data Produk
# users: {username: [password, role]}
users = {"komang": ["003", "admin"]} 
# produk: {nama_produk: {'stok': stok_int, 'harga': harga_int}}
produk = {
    "Net Volly": {'stok': 15, 'harga': 170000},
    "Hand Grip": {'stok': 10, 'harga': 100000},
    "Papan Skor": {'stok': 10, 'harga': 150000},
    "Bola Kasti": {'stok': 25, 'harga': 25000},
    "Sepatu Futsal": {'stok': 15, 'harga': 499000}
}
        
# Program Utama
while True:
    # Membersihkan terminal sebelum menu
    os.system("cls" if os.name == "nt" else "clear")

    print("|===================================================|")
    print("|     MENU UTAMA - TOKO PERLENGKAPAN OLAHRAGA       |")
    print("|===================================================|")
    print("|1. Login                                           |")
    print("|2. Register                                        |")
    print("|3. Keluar                                          |")
    print("|===================================================|")
    pilih = input("Pilih 1, 2, atau 3, yuk: ")

    if pilih == "1":
        # LOGIN
        os.system("cls" if os.name == "nt" else "clear")
        print("|==================================================|")
        print("|                  LOGIN AKUN                      |")
        print("|==================================================|")
        username = input("masukkan username kamu dong: ")
        password = input("password nya juga ya: ")

        # Cek Hasil Login
        if username in users and users[username][0] == password:
            role = users[username][1]
            print(f"\nLogin berhasil! Selamat datang, {username}")
            input("Tekan Enter untuk lanjut...")

            # Kalau dia Admin Muncul Menu Ini
            if role == "admin":
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("|==================================================|")
                    print("|                  MENU ADMIN                      |")
                    print("|==================================================|")
                    print("|1. Lihat Produk                                   |")
                    print("|2. Tambah Produk                                  |")
                    print("|3. Update Produk                                  |")
                    print("|4. Hapus Produk                                   |")
                    print("|5. Logout                                         |")
                    print("|==================================================|")
                    menu_admin = input("Pilih menu 1-5 yuk: ")

                    if menu_admin == "1":
                        # LIHAT PRODUK (ADMIN)
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                DAFTAR PRODUK                     |")
                        print("|==================================================|")
                        if not produk:
                            print("Belum ada produk.")
                        else:
                            nomor = 1
                            # Ambil nama (key) dan data detail (value) dari setiap produk
                            for nama, data in produk.items():
                                # Kita ambil data stok dan harga dari detail produk
                                print(f"{nomor}. {nama} - Stok: {data['stok']} - Harga: Rp {data['harga']:,}")
                                nomor += 1
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "2":
                        # TAMBAH PRODUK
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|              TAMBAH PRODUK BARU                  |")
                        print("|==================================================|")
                        nama = input("Nama produk: ")
                        
                        # Error Handling: Nama kosong atau sudah ada
                        if nama == "":
                            print("Nama produk tidak boleh kosong!")
                        elif nama in produk:
                            print("Produk dengan nama tersebut sudah ada!")
                        else:
                            stok_str = input("Stok: ")
                            harga_str = input("Harga: ")

                            # Pastikan inputan stok dan harga itu benar benar angka
                            if stok_str.isdigit() and harga_str.isdigit() and int(stok_str) > 0 and int(harga_str) > 0:
                                # Masukkan Daftar Produk Baru ke Daftar
                                produk[nama] = {'stok': int(stok_str), 'harga': int(harga_str)}
                                print(f"Produk '{nama}' berhasil ditambahkan!")
                            else:
                                print("Stok dan harga harus berupa angka!")
                        input("Tekan Enter untuk kembali...")

                    elif menu_admin == "3":
                        # UPDATE PRODUK
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                UPDATE PRODUK                     |")
                        print("|==================================================|")
                        
                        # Tampilkan produk untuk dipilih
                        if not produk:
                            print("Belum ada produk.")
                            input("Tekan Enter untuk kembali...")
                            continue

                        nomor = 1
                        # Siapkan daftar produk
                        list_nama_produk = list(produk.keys()) 
                        for nama in list_nama_produk:
                            data = produk[nama]
                            # Mengakses data menggunakan keys 'stok' dan 'harga'
                            print(f"{nomor}. {nama} (Stok: {data['stok']}, Harga: {data['harga']:,})")
                            nomor += 1
                        print("|==================================================|")

                        nomor_str = input("\nMasukkan nomor produk yang ingin diupdate: ")
                        
                        # Error Handling: Input harus angka
                        if nomor_str.isdigit():
                            nomor = int(nomor_str)
                            # Error Handling: cek nomor produk yang diinput ada di daftar (1 sampai akhir)
                            if nomor >= 1 and nomor <= len(produk):
                                nama_lama = list_nama_produk[nomor - 1]
                                data_lama = produk[nama_lama]

                                print(f"\n--- Update Produk: {nama_lama} ---")
                                nama_baru = input(f"Nama baru (kosongkan: '{nama_lama}'): ")
                                stok_baru_str = input(f"Stok baru (kosongkan: {data_lama['stok']}): ")
                                harga_baru_str = input(f"Harga baru (kosongkan: {data_lama['harga']}): ")

                                update_berhasil = False
                                
                                # 1. Update Nama
                                if nama_baru != "" and nama_baru != nama_lama:
                                    if nama_baru not in produk:
                                        # Ganti nama lama dengan nama baru, datanya tetap aman!
                                        produk[nama_baru] = produk.pop(nama_lama) 
                                        nama_lama = nama_baru 
                                        # Ganti nama lama untuk update selanjutnya
                                        update_berhasil = True
                                    else:
                                        print("Nama produk baru sudah ada! Nama tidak diubah.")
                                
                                # 2. Jangan lupa, update nilai stoknya 
                                if stok_baru_str.isdigit() and int(stok_baru_str) >= 0:
                                    produk[nama_lama]['stok'] = int(stok_baru_str)
                                    update_berhasil = True
                                elif stok_baru_str != "":
                                    print("Stok harus berupa angka positif! Stok tidak diubah.")

                                # 3. Jangan lupa, update harga jualnya 
                                if harga_baru_str.isdigit() and int(harga_baru_str) >= 0:
                                    produk[nama_lama]['harga'] = int(harga_baru_str)
                                    update_berhasil = True
                                elif harga_baru_str != "":
                                    print("Harga harus berupa angka! Harga tidak diubah.")
                                    
                                if update_berhasil:
                                    print("\nData produk berhasil diperbarui!")
                                else:
                                    print("\nTidak ada perubahan yang valid dilakukan.")

                            else:
                                print("Nomor produk tidak ditemukan!")
                        else:
                            print("Input harus berupa angka!")
                        
                        input("Tekan Enter untuk kembali...")

                    elif menu_admin == "4":
                        # HAPUS PRODUK
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                  HAPUS PRODUK                    |")
                        print("|==================================================|")
                        
                        # Tampilkan produk untuk dipilih
                        if not produk:
                            print("Belum ada produk.")
                            input("Tekan Enter untuk kembali...")
                            continue

                        nomor = 1
                        list_nama_produk = list(produk.keys()) # Ubah keys produk jadi list, agar bisa dihitung 1, 2, 3...
                        for nama in list_nama_produk:
                            data = produk[nama]
                            print(f"{nomor}. {nama} (Stok: {data['stok']}, Harga: {data['harga']:,})")
                            nomor += 1

                        hapus_str = input("\nMasukkan nomor produk yang ingin dihapus: ")
                        
                        # Error Handling: Input harus angka
                        if hapus_str.isdigit():
                            hapus_nomor = int(hapus_str)
                            # Error Handling: cek nomor produk yang diinput ada di daftar (1 sampai akhir)
                            if hapus_nomor >= 1 and hapus_nomor <= len(produk):
                                nama_produk_dihapus = list_nama_produk[hapus_nomor - 1]
                                # Menghapus item dari dictionary berdasarkan key
                                del produk[nama_produk_dihapus]
                                print(f"Produk '{nama_produk_dihapus}' berhasil dihapus!")
                            else:
                                print("Nomor produk tidak ditemukan!")
                        else:
                            print("Input tidak valid!")
                        
                        input("Tekan Enter untuk kembali...")

                    elif menu_admin == "5":
                        print("Logout berhasil!")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk coba lagi...")

            # MENU USER
            else: # role == "user"
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("|==================================================|")
                    print("|                  MENU PENGGUNA                   |")
                    print("|==================================================|")
                    print("|1. Lihat Produk                                   |")
                    print("|2. Logout                                         |")
                    print("|==================================================|")
                    pilih_user = input("Pilih menu 1-2: ")

                    if pilih_user == "1":
                        # LIHAT PRODUK (USER)
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                DAFTAR PRODUK                     |")
                        print("|==================================================|")
                        if not produk:
                            print("Belum ada produk.")
                        else:
                            nomor = 1
                            for nama, data in produk.items():
                                # Mengakses data menggunakan keys 'stok' dan 'harga'
                                print(f"{nomor}. {nama} - Stok: {data['stok']} - Harga: Rp {data['harga']:,}")
                                nomor += 1
                        input("\nTekan Enter untuk kembali...")
                    elif pilih_user == "2":
                        print("Logout berhasil! Terima kasih sudah mampir")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Tekan Enter untuk coba lagi...")
        else:
            print("\nUsername atau password salah!")
            input("Tekan Enter untuk coba lagi...")

    elif pilih == "2":
        # REGISTER
        os.system("cls" if os.name == "nt" else "clear")
        print("|==================================================|")
        print("|              REGISTER AKUN BARU                  |")
        print("|==================================================|")
        username = input("Username: ")
        password = input("Password: ")

        # Error Handling: Username atau password kosong
        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
        # Error Handling: Username sudah digunakan (cek di dictionary keys)
        elif username in users:
            print("Username sudah digunakan!")
        else:
            # Tambahkan user baru ke dictionary users
            users[username] = [password, "user"]
            print("Akun berhasil dibuat!")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilih == "3":
        # KELUAR
        os.system("cls" if os.name == "nt" else "clear")
        print("Terima kasih sudah berkunjung di toko kami")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk coba lagi...")