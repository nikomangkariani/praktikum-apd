import os
os.system("cls" if os.name == "nt" else "clear")

#Salam Pembuka
print("|===============================================================|")
print("|         SELAMAT DATANG DI TOKO PERLENGKAPAN OLAHRAGA          |")
print("|===============================================================|")
print("Halo!")
print("Selamat datang di toko perlengkapan olahraga kami")
print("Di sini kamu bisa beli perlengkapan olahraga favoritmu loh.\n")
input("Tekan Enter ya untuk lanjut ke menu..")
        
#data awal
users = [["komang", "003", "admin"]]
produk = [
    ["Net Volly", 15, 170000],
    ["Hand Grip", 10, 100000],
    ["Papan Skor", 10, 150000],
    ["Bola Kasti", 25, 25000],
    ["Sepatu Futsal", 15, 499000]
]

#program awal
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("|===================================================|")
    print("|    MENU UTAMA - TOKO PERLENGKAPAN OLAHRAGA        |")
    print("|===================================================|")
    print("|1. Login                                           |")
    print("|2. Register                                        |")
    print("|3. Keluar                                          |")
    print("|===================================================|")
    pilih = input("Pilih menu 1-3: ")

    if pilih == "1":
        #LOGIN
        os.system("cls" if os.name == "nt" else "clear")
        print("|==================================================|")
        print("|                  LOGIN AKUN                      |")
        print("|==================================================|")
        username = input("masukkan username kamu dong: ")
        password = input("password nya juga ya: ")

        login_berhasil = False
        role = ""
        i = 0
        while i < len(users):
            if users[i][0] == username and users[i][1] == password:
                login_berhasil = True
                role = users[i][2]
                break
            i = i + 1

        if login_berhasil:
            print(f"\nLogin berhasil! Selamat datang, {username}")
            input("Tekan Enter untuk lanjut...")

            #Menu Admin
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
                    menu_admin = input("Pilih menu 1-5: ")

                    if menu_admin == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                  DAFTAR PRODUK                   |")
                        print("|==================================================|")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            i = 0
                            while i < len(produk):
                                print(f"{i+1}. {produk[i][0]} - Stok: {produk[i][1]} - Harga: Rp {produk[i][2]}")
                                i = i + 1
                        input("\nTekan Enter untuk kembali...")

                    elif menu_admin == "2":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                 TAMBAH PRODUK BARU               |")
                        print("|==================================================|")
                        nama = input("Nama produk: ")
                        
                        if nama == "":
                            print("Nama produk tidak boleh kosong!")
                            input("Tekan Enter untuk kembali...")
                        else:
                            stok = input("Stok: ")
                            harga = input("Harga: ")

                            if stok.isdigit() and harga.isdigit():
                                produk.append([nama, int(stok), int(harga)])
                                print("Produk berhasil ditambahkan!")
                            else:
                                print("Stok dan harga harus berupa angka!")
                            input("Tekan Enter untuk kembali...")

                    elif menu_admin == "3":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                  UPDATE PRODUK                   |")
                        print("|==================================================|")
                        i = 0
                        while i < len(produk):
                            print(f"{i+1}. {produk[i][0]} (Stok: {produk[i][1]}, Harga: {produk[i][2]})")
                            i = i + 1
                        print("|==================================================|")
                        nomor = input("\nMasukkan nomor produk yang ingin diupdate: ")
                        if nomor.isdigit():
                            nomor = int(nomor) - 1
                            if nomor >= 0 and nomor < len(produk):
                                nama_baru = input("Nama baru (kosongkan jika tidak diubah): ")
                                stok_baru = input("Stok baru (kosongkan jika tidak diubah): ")
                                harga_baru = input("Harga baru (kosongkan jika tidak diubah): ")

                                if nama_baru != "":
                                    produk[nomor][0] = nama_baru
                                if stok_baru.isdigit():
                                    produk[nomor][1] = int(stok_baru)
                                if harga_baru.isdigit():
                                    produk[nomor][2] = int(harga_baru)
                                print("Data produk berhasil diperbarui!")
                            else:
                                print("Nomor produk tidak ditemukan!")
                        else:
                            print("Input harus berupa angka!")
                        input("Tekan Enter untuk kembali...")

                    elif menu_admin == "4":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                   HAPUS PRODUK                   |")
                        print("|==================================================|")
                        i = 0
                        while i < len(produk):
                            print(f"{i+1}. {produk[i][0]} (Stok: {produk[i][1]}, Harga: {produk[i][2]})")
                            i = i + 1
                        hapus = input("\nMasukkan nomor produk yang ingin dihapus: ")
                        if hapus.isdigit():
                            hapus = int(hapus) - 1
                            if hapus >= 0 and hapus < len(produk):
                                produk.pop(hapus)
                                print("Produk berhasil dihapus!")
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

            #MENU USER
            else:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("|==================================================|")
                    print("|                   MENU PENGGUNA                  |")
                    print("|==================================================|")
                    print("|1. Lihat Produk                                   |")
                    print("|2. Logout                                         |")
                    print("|==================================================|")
                    pilih_user = input("Pilih menu 1-2: ")

                    if pilih_user == "1":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("|==================================================|")
                        print("|                   DAFTAR PRODUK                  |")
                        print("|==================================================|")
                        if len(produk) == 0:
                            print("Belum ada produk.")
                        else:
                            i = 0
                            while i < len(produk):
                                print(f"{i+1}. {produk[i][0]} - Stok: {produk[i][1]} - Harga: Rp {produk[i][2]}")
                                i = i + 1
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
        #REGISTER
        os.system("cls" if os.name == "nt" else "clear")
        print("|==================================================|")
        print("|               REGISTER AKUN BARU                 |")
        print("|==================================================|")
        username = input("Username: ")
        password = input("Password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong!")
        else:
            sudah_ada = False
            i = 0
            while i < len(users):
                if users[i][0] == username:
                    sudah_ada = True
                    break
                i = i + 1

            if sudah_ada:
                print("Username sudah digunakan!")
            else:
                users.append([username, password, "user"])
                print("Akun berhasil dibuat!")
        input("Tekan Enter untuk kembali ke menu utama...")

    elif pilih == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("Terima kasih sudah berkunjung di toko kami")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk coba lagi...")