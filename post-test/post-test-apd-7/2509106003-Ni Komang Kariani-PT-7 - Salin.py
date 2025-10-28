import os

# Data utama program
users = {"komang": ["003", "admin"]} 
produk = {
    "Net Volly": {'stok': 15, 'harga': 170000},
    "Hand Grip": {'stok': 10, 'harga': 100000},
    "Papan Skor": {'stok': 10, 'harga': 150000},
    "Bola Kasti": {'stok': 25, 'harga': 25000},
    "Sepatu Futsal": {'stok': 15, 'harga': 499000}
}
keranjang_belanja = {}

# Fungsi dengan parameter - buat hitung total belanja
def hitung_total(nama_user):
    total_harga = 0
    try:
        if nama_user in keranjang_belanja:
            for barang in keranjang_belanja[nama_user]:
                harga_item = barang['jumlah'] * barang['harga']
                total_harga += harga_item
        return total_harga
    except:
        print("Waduh ada error saat hitung total")
        return 0

# Fungsi rekursif dengan parameter - buat cari produk
def cari_barang(daftar_produk, kata_kunci, idx=0, ketemu=None):
    if ketemu is None:
        ketemu = []
    
    if idx >= len(daftar_produk):
        return ketemu
    
    nama = daftar_produk[idx]
    if kata_kunci.lower() in nama.lower():
        ketemu.append(nama)
    
    return cari_barang(daftar_produk, kata_kunci, idx + 1, ketemu)

# Fungsi tanpa parameter - buat bersihin layar dan tampilkan header
def tampil_header():
    os.system("cls" if os.name == "nt" else "clear")
    print("|===============================================================|")
    print("|       SELAMAT DATANG DI TOKO PERLENGKAPAN OLAHRAGA            |")
    print("|===============================================================|")
    return True

# Fungsi tanpa parameter - hitung total stok barang
def total_stok_barang():
    jumlah = 0
    try:
        for nama, info in produk.items():
            jumlah += info['stok']
        return jumlah
    except:
        print("Error saat menghitung stok")
        return 0

# Prosedur - menampilkan nota belanja
def cetak_nota(nama_user):
    os.system("cls" if os.name == "nt" else "clear")
    print("|==================================================|")
    print("|              NOTA BELANJA ANDA                   |")
    print("|==================================================|")
    
    if nama_user not in keranjang_belanja or len(keranjang_belanja[nama_user]) == 0:
        print("Keranjang masih kosong nih!")
        return
    
    no = 1
    print(f"Pembeli: {nama_user}")
    print("-" * 50)
    
    for item in keranjang_belanja[nama_user]:
        nama_barang = item['nama']
        banyak = item['jumlah']
        harga_satuan = item['harga']
        subtotal_harga = banyak * harga_satuan
        print(f"{no}. {nama_barang}")
        print(f"   {banyak} x Rp {harga_satuan:,} = Rp {subtotal_harga:,}")
        no += 1
    
    print("-" * 50)
    total_bayar = hitung_total(nama_user)
    print(f"TOTAL PEMBAYARAN: Rp {total_bayar:,}")
    print("|==================================================|")

# Prosedur - untuk kosongin keranjang
def kosongin_keranjang(nama_user):
    try:
        if nama_user in keranjang_belanja:
            keranjang_belanja[nama_user] = []
            print("Keranjang sudah dikosongkan!")
        else:
            print("Keranjang sudah kosong dari tadi kok")
    except:
        print("Error saat kosongin keranjang")

# Fungsi untuk validasi input angka
def cek_angka(input_user, nama_input="Input"):
    try:
        if not input_user.strip():
            print(f"{nama_input} jangan kosong dong!")
            return None
        
        angka = int(input_user)
        if angka < 0:
            print(f"{nama_input} gak boleh minus!")
            return None
        return angka
    except ValueError:
        print(f"{nama_input} harus angka ya!")
        return None

# Program dimulai dari sini
tampil_header()
print("Hai! Lagi nyari perlengkapan olahraga ya?")
print("Yuk cek-cek dulu produk kita\n")
input("Tekan Enter untuk lanjut ya..")

while True:
    tampil_header()
    print("|===================================================|")
    print("|                  MENU UTAMA TOKO                  |")
    print("|===================================================|")
    print("|1. Login                                           |")
    print("|2. Daftar Akun Baru                                |")
    print("|3. Keluar                                          |")
    print("|===================================================|")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        # Proses login
        tampil_header()
        print("|==================================================|")
        print("|                  LOGIN DULU YUK                  |")
        print("|==================================================|")
        user = input("Username kamu: ")
        pw = input("Password: ")

        if user in users and users[user][0] == pw:
            tipe_user = users[user][1]
            print(f"\nLogin sukses! Hai {user} Selamat Datang")
            input("Enter untuk lanjut...")

            # Jika yang login adalah admin
            if tipe_user == "admin":
                while True:
                    tampil_header()
                    print("|==================================================|")
                    print("|                   MENU ADMIN                     |")
                    print("|==================================================|")
                    print("|1. Lihat Produk                                   |")
                    print("|2. Tambah Produk Baru                             |")
                    print("|3. Update Produk                                  |")
                    print("|4. Hapus Produk                                   |")
                    print("|5. Cari Produk                                    |")
                    print("|6. Cek Total Stok                                 |")
                    print("|7. Logout                                         |")
                    print("|==================================================|")
                    menu = input("Pilih menu yuk? (1-7): ")

                    if menu == "1":
                        # Lihat produk
                        tampil_header()
                        print("|==================================================|")
                        print("|              DAFTAR PRODUK TOKO                  |")
                        print("|==================================================|")
                        if not produk:
                            print("Belum ada produk nih")
                        else:
                            nomor = 1
                            for nama_produk, data in produk.items():
                                print(f"{nomor}. {nama_produk} | Stok: {data['stok']} | Harga: Rp {data['harga']:,}")
                                nomor += 1
                        input("\nTekan enter untuk kembali...")

                    elif menu == "2":
                        # Tambah produk
                        tampil_header()
                        print("|==================================================|")
                        print("|                TAMBAH PRODUK                     |")
                        print("|==================================================|")
                        nama_baru = input("Nama produk: ").strip()
                        
                        try:
                            if not nama_baru:
                                print("Namanya jangan kosong dong!")
                            elif nama_baru in produk:
                                print("Produk ini udah ada di list!")
                            else:
                                stok_input = input("Stok: ")
                                harga_input = input("Harga: ")

                                stok_angka = cek_angka(stok_input, "Stok")
                                harga_angka = cek_angka(harga_input, "Harga")

                                if stok_angka is not None and harga_angka is not None:
                                    if stok_angka > 0 and harga_angka > 0:
                                        produk[nama_baru] = {'stok': stok_angka, 'harga': harga_angka}
                                        print(f"Oke, '{nama_baru}' sudah ditambahkan!")
                                    else:
                                        print("Stok sama harga harus lebih dari 0 ya!")
                        except Exception as e:
                            print(f"Ada error nih: {e}")
                        
                        input("Enter untuk kembali...")

                    elif menu == "3":
                        # Update produk
                        tampil_header()
                        print("|==================================================|")
                        print("|                   UPDATE PRODUK                  |")
                        print("|==================================================|")
                        
                        if not produk:
                            print("Belum ada produk yang bisa diedit")
                            input("Enter untuk balik...")
                            continue

                        nomor = 1
                        daftar_nama = list(produk.keys())
                        for nama_produk in daftar_nama:
                            info = produk[nama_produk]
                            print(f"{nomor}. {nama_produk} (Stok: {info['stok']}, Harga: {info['harga']:,})")
                            nomor += 1
                        print("|==================================================|")

                        pilih_nomor = input("\nPilih nomor produk yang ingin di Update: ")
                        
                        try:
                            nomor_dipilih = cek_angka(pilih_nomor, "Nomor")
                            if nomor_dipilih is None:
                                print("Input tidak valid!")
                            elif nomor_dipilih < 1 or nomor_dipilih > len(produk):
                                print("Nomor produk tidak ada!")
                            else:
                                nama_lama = daftar_nama[nomor_dipilih - 1]
                                data_lama = produk[nama_lama]

                                print(f"\n--- Edit Produk: {nama_lama} ---")
                                nama_baru = input(f"Nama baru (kosongkan jika tidak ingin ganti): ").strip()
                                stok_baru = input(f"Stok baru (sekarang {data_lama['stok']}): ")
                                harga_baru = input(f"Harga baru (sekarang {data_lama['harga']}): ")

                                ada_perubahan = False
                                
                                if nama_baru and nama_baru != nama_lama:
                                    if nama_baru not in produk:
                                        produk[nama_baru] = produk.pop(nama_lama)
                                        nama_lama = nama_baru
                                        ada_perubahan = True
                                    else:
                                        print("Nama baru sudah dipakai produk lain!")
                                
                                if stok_baru:
                                    stok_angka = cek_angka(stok_baru, "Stok")
                                    if stok_angka is not None:
                                        produk[nama_lama]['stok'] = stok_angka
                                        ada_perubahan = True

                                if harga_baru:
                                    harga_angka = cek_angka(harga_baru, "Harga")
                                    if harga_angka is not None:
                                        produk[nama_lama]['harga'] = harga_angka
                                        ada_perubahan = True
                                    
                                if ada_perubahan:
                                    print("\nProduk berhasil diupdate!")
                                else:
                                    print("\nTidak ada yang diubah nih")

                        except Exception as e:
                            print(f"Ada error: {e}")
                        
                        input("Enter untuk kembali...")

                    elif menu == "4":
                        # Hapus produk
                        tampil_header()
                        print("|==================================================|")
                        print("|                    HAPUS PRODUK                  |")
                        print("|==================================================|")
                        
                        if not produk:
                            print("Belum ada produk yang bisa dihapus")
                            input("Enter untuk kembali...")
                            continue

                        nomor = 1
                        daftar_nama = list(produk.keys())
                        for nama_produk in daftar_nama:
                            info = produk[nama_produk]
                            print(f"{nomor}. {nama_produk} (Stok: {info['stok']}, Harga: {info['harga']:,})")
                            nomor += 1

                        pilih_hapus = input("\nPilih nomor produk yang ingin dihapus: ")
                        
                        try:
                            nomor_hapus = cek_angka(pilih_hapus, "Nomor")
                            if nomor_hapus is None:
                                print("Input tidak valid!")
                            elif nomor_hapus < 1 or nomor_hapus > len(produk):
                                print("Nomor produk tidak ada!")
                            else:
                                nama_dihapus = daftar_nama[nomor_hapus - 1]
                                del produk[nama_dihapus]
                                print(f"Produk '{nama_dihapus}' berhasil dihapus!")
                        except Exception as e:
                            print(f"Ada error: {e}")
                        
                        input("Enter untuk kembali...")

                    elif menu == "5":
                        # Cari produk menggunakan rekursif
                        tampil_header()
                        print("|==================================================|")
                        print("|                    CARI PRODUK                   |")
                        print("|==================================================|")
                        
                        if not produk:
                            print("Belum ada produk nih")
                        else:
                            kata_cari = input("Mau cari produk apa? ").strip()
                            if kata_cari:
                                list_produk = list(produk.keys())
                                hasil_cari = cari_barang(list_produk, kata_cari)
                                
                                if hasil_cari:
                                    print(f"\nketemu {len(hasil_cari)} produk:")
                                    for i, nama_produk in enumerate(hasil_cari, 1):
                                        info = produk[nama_produk]
                                        print(f"{i}. {nama_produk} | Stok: {info['stok']} | Harga: Rp {info['harga']:,}")
                                else:
                                    print("Gak ketemu nih produknya")
                            else:
                                print("Kata kuncinya jangan kosong!")
                        
                        input("\nEnter untuk kembali...")

                    elif menu == "6":
                        # Cek total stok
                        tampil_header()
                        print("|==================================================|")
                        print("|                  CEK TOTAL STOK                  |")
                        print("|==================================================|")
                        total = total_stok_barang()
                        print(f"Total semua stok produk: {total} unit")
                        input("\nEnter untuk kembali...")

                    elif menu == "7":
                        print("Oke, logout dulu ya!")
                        input("Enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("Pilihan tidak ada!")
                        input("Enter untuk coba lagi...")

            # Jika yang login adalah user biasa
            else:
                if user not in keranjang_belanja:
                    keranjang_belanja[user] = []
                
                while True:
                    tampil_header()
                    print("|==================================================|")
                    print("|                  MENU USER BIASA                 |")
                    print("|==================================================|")
                    print("|1. Lihat Produk                                   |")
                    print("|2. Cari Produk                                    |")
                    print("|3. Tambah ke Keranjang                            |")
                    print("|4. Cek Keranjang                                  |")
                    print("|5. Bayar (Checkout)                               |")
                    print("|6. Kosongkan Keranjang                            |")
                    print("|7. Logout                                         |")
                    print("|==================================================|")
                    pilihan_user = input("pilih yuk? (1-7): ")

                    if pilihan_user == "1":
                        # Lihat produk
                        tampil_header()
                        print("|==================================================|")
                        print("|              DAFTAR PRODUK TOKO                  |")
                        print("|==================================================|")
                        if not produk:
                            print("Belum ada produk nih")
                        else:
                            nomor = 1
                            for nama_produk, data in produk.items():
                                print(f"{nomor}. {nama_produk} | Stok: {data['stok']} | Harga: Rp {data['harga']:,}")
                                nomor += 1
                        input("\nEnter untuk kembali...")

                    elif pilihan_user == "2":
                        # Cari produk
                        tampil_header()
                        print("|==================================================|")
                        print("|                   CARI PRODUK                    |")
                        print("|==================================================|")
                        
                        if not produk:
                            print("Belum ada produk nih")
                        else:
                            kata_cari = input("Mau cari apa? ").strip()
                            if kata_cari:
                                list_produk = list(produk.keys())
                                hasil_cari = cari_barang(list_produk, kata_cari)
                                
                                if hasil_cari:
                                    print(f"\n1 produk ketemu {len(hasil_cari)} produk:")
                                    for i, nama_produk in enumerate(hasil_cari, 1):
                                        info = produk[nama_produk]
                                        print(f"{i}. {nama_produk} | Stok: {info['stok']} | Harga: Rp {info['harga']:,}")
                                else:
                                    print("Gak ketemu nih produknya")
                            else:
                                print("Kata kuncinya jangan kosong!")
                        
                        input("\nEnter untuk kembali...")

                    elif pilihan_user == "3":
                        # Tambah ke keranjang
                        tampil_header()
                        print("|==================================================|")
                        print("|                MASUKKAN KE KERANJANG             |")
                        print("|==================================================|")
                        
                        if not produk:
                            print("Belum ada produk yang bisa dibeli")
                            input("Enter untuk kembali...")
                            continue

                        nomor = 1
                        daftar_nama = list(produk.keys())
                        for nama_produk in daftar_nama:
                            info = produk[nama_produk]
                            print(f"{nomor}. {nama_produk} | Stok: {info['stok']} | Harga: Rp {info['harga']:,}")
                            nomor += 1

                        try:
                            pilih = input("\nPilih nomor produk: ")
                            nomor_pilih = cek_angka(pilih, "Nomor")
                            
                            if nomor_pilih is None:
                                print("Input tidak valid!")
                            elif nomor_pilih < 1 or nomor_pilih > len(produk):
                                print("Nomor produk tidak ada!")
                            else:
                                nama_produk = daftar_nama[nomor_pilih - 1]
                                info_produk = produk[nama_produk]
                                
                                if info_produk['stok'] == 0:
                                    print("Waduh stoknya habis!")
                                else:
                                    jumlah_beli = input(f"Mau beli berapa? (max {info_produk['stok']}): ")
                                    jumlah = cek_angka(jumlah_beli, "Jumlah")
                                    
                                    if jumlah is None or jumlah <= 0:
                                        print("Jumlahnya harus lebih dari 0!")
                                    elif jumlah > info_produk['stok']:
                                        print(f"Stok gak cukup! hanya ada {info_produk['stok']} unit")
                                    else:
                                        keranjang_belanja[user].append({
                                            'nama': nama_produk,
                                            'jumlah': jumlah,
                                            'harga': info_produk['harga']
                                        })
                                        print(f"\nOke! {jumlah} {nama_produk} sudah masuk keranjang")
                                
                        except Exception as e:
                            print(f"Ada error: {e}")
                        
                        input("Enter untuk kembali...")

                    elif pilihan_user == "4":
                        # Lihat keranjang
                        cetak_nota(user)
                        input("\nEnter untuk kembali...")

                    elif pilihan_user == "5":
                        # Checkout
                        cetak_nota(user)
                        
                        if user in keranjang_belanja and len(keranjang_belanja[user]) > 0:
                            konfirmasi = input("\nJadi bayar sekarang? (y/n): ").lower()
                            
                            if konfirmasi == 'y':
                                try:
                                    for item in keranjang_belanja[user]:
                                        nama_item = item['nama']
                                        jumlah_item = item['jumlah']
                                        if nama_item in produk:
                                            produk[nama_item]['stok'] -= jumlah_item
                                    
                                    print("\n✓ Pembayaran sukses!")
                                    print("Terima kasih sudah belanja di toko kita ya!")
                                    kosongin_keranjang(user)
                                except Exception as e:
                                    print(f"Ada error saat checkout: {e}")
                            else:
                                print("Oke, checkout dibatalkan")
                        
                        input("Enter untuk kembali...")

                    elif pilihan_user == "6":
                        # Kosongkan keranjang
                        tampil_header()
                        print("|==================================================|")
                        print("|          KOSONGKAN KERANJANG                     |")
                        print("|==================================================|")
                        kosongin_keranjang(user)
                        input("Enter untuk kembali...")

                    elif pilihan_user == "7":
                        print("Oke, logout dulu ya!")
                        input("Enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("Pilihan tidak ada!")
                        input("Enter untuk coba lagi...")
        else:
            print("\nUsername atau password salah nih!")
            input("Enter untuk coba lagi...")

    elif pilihan == "2":
        # Register
        tampil_header()
        print("|==================================================|")
        print("|              DAFTAR AKUN BARU                    |")
        print("|==================================================|")
        user_baru = input("Username: ").strip()
        pw_baru = input("Password: ")

        try:
            if not user_baru or not pw_baru:
                print("Username sama password tidak boleh kosong!")
            elif user_baru in users:
                print("Username sudah dipakai orang lain!")
            else:
                users[user_baru] = [pw_baru, "user"]
                print("Akun berhasil dibuat! Sekarang bisa login")
        except Exception as e:
            print(f"Ada error: {e}")
        
        input("Enter untuk kembali ke menu utama...")

    elif pilihan == "3":
        # Keluar
        tampil_header()
        print("Terima kasih sudah mampir ke toko kita!")
        print("Sampai jumpa lagi ya!")
        break

    else:
        print("Pilihan tidak ada!")
        input("Enter buat coba lagi...")
