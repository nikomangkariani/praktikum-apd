while True:
    print("=======================================")
    print("|  Halo! Selamat datang di Toko Miming |")
    print("=======================================")
    print("| Yuk login dulu biar dapet diskon 15% |")
    print("=======================================")

    # variabel
    keranjang = ""
    total_belanja = 0
    diskon = 0
    login_berhasil = False
    non_member = True

    # Login
    status = input("Kamu mau login sebagai member? (y/n): ").lower()

    if status == 'y':
        print("\n----------------------------")
        print("|        LOGIN MEMBER        |")
        print("----------------------------")
        for i in range(3):
            username = input("Username kamu: ")
            password = input("Password nya apa?: ")
            if username == "komang" and password == "003":
                print("----------------------------")
                print(" Sip! Kamu berhasil login  ")
                print("----------------------------")
                login_berhasil = True
                non_member = False
                break
            else:
                print(f"Oops, salah. Sisa percobaan: {2 - i}")
        if not login_berhasil:
            print("----------------------------------------------------")
            print("|Gagal login 3 kali. Kamu lanjut sebagai non-member |")
            print("----------------------------------------------------")
    elif status == 'n':
        print("--------------------------------------------")
        print(" Oke, kamu belanja sebagai non-member ya ")
        print("--------------------------------------------")
    else:
        print("--------------------------------------------")
        print(" Input tidak dikenali. Kamu lanjut sebagai non-member ")
        print("--------------------------------------------")

    # Menu Belanja
    while True:
        print("\n----------------------------")
        print("|         MENU BELANJA       |")
        print("----------------------------")
        print("| 1. Tambah Produk           |")
        print("| 2. Checkout                |")
        print("----------------------------")
        pilihan = input("Mau pilih yang mana? (1/2): ")

        if pilihan == '1':
            print("\n----------------------------")
            print("|        DAFTAR PRODUK        |")
            print("----------------------------")
            print(" 1. Jersey         Rp 100000")
            print(" 2. Sepatu Victor  Rp 700000")
            print(" 3. Raket Yonex    Rp1500000")
            print(" 4. Grip           Rp 10000 ")
            print(" 5. Tas Olahraga   Rp 250000")
            print("--------------------------------------------")
            pilih = input("Mau beli yang mana? Ketik nomornya: ")

            if pilih == '1':
                keranjang += "- Jersey: Rp 100000\n"
                total_belanja += 100000
            elif pilih == '2':
                keranjang += "- Sepatu Victor: Rp 700000\n"
                total_belanja += 700000
            elif pilih == '3':
                keranjang += "- Raket Yonex: Rp 1500000\n"
                total_belanja += 1500000
            elif pilih == '4':
                keranjang += "- Grip: Rp 10000\n"
                total_belanja += 10000
            elif pilih == '5':
                keranjang += "- Tas Olahraga: Rp 250000\n"
                total_belanja += 250000
            else:
                print("Nomor produk tidak ada, coba lagi ya!")
                continue

            print("Produk sudah masuk ke keranjang!")
            print(f"Total sementara: Rp {total_belanja}")
        elif pilihan == '2':
            break
        else:
            print("Pilihan tidak valid. Ketik 1 atau 2 ya!")

    # Checkout
    print("\n----------------------------")
    print("|      STRUK BELANJA         |")
    print("------------------------------")
    print(keranjang)
    print("----------------------------")

    if not non_member:
        diskon = total_belanja * 0.15
        print(f" Total Sebelum Diskon : Rp {total_belanja}")
        print(f" Diskon 15%            : Rp {diskon}")
        print(f" Total Bayar           : Rp {total_belanja - diskon}")
    else:
        print(f" Total Bayar           : Rp {total_belanja}")
    print("-----------------------------------------")

    # Transaksi Baru
    print("\n---------------------------------------")
    print("| Mau belanja lagi nggak? (y/n)         |")
    print("-----------------------------------------")
    ulang = input("Jawab y atau n: ").lower()
    if ulang == 'y':
        continue
    elif ulang == 'n':
        print("\n----------------------------------")
        print("|Terimakasi sudah belanja di sini  |")
        print("------------------------------------")
        break
    else:
        print("Input tidak dikenali. Program selesai.")
        break

       

