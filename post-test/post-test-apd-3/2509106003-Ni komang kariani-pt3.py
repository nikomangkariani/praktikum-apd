# Sistem Belanja JS Family Store

print("Selamat datang di JS Family Store!")
is_member = input("Apakah Anda Member JS Family? (ya/tidak):").lower() == "ya"

if is_member:
    username = input("Username: ")
    password = input("Password: ")
    if username != "Komang" or password != "003":
        print("Login gagal. Username atau password salah.")
        exit()
    print("Login berhasil")

print("MENU PRODUK JS FAMILY:")
print("1. Facewash - Rp120000")
print("2. Mask     - Rp60000")
print("3. Toner    - Rp135000")

pilih = input("Pilih produk (1/2/3): ")
jumlah = int(input("Jumlah yang dibeli: "))

if pilih == "1":
    nama = "Facewash"
    harga = 120000
elif pilih == "2":
    nama = "Mask"
    harga = 60000
elif pilih == "3":
    nama = "Toner"
    harga = 135000
else:
    nama = "-"
    harga = 0
    jumlah = 0
    
total = harga * jumlah
diskon = total * 0.15 if is_member else 0
bayar = total - diskon
print("\n--- STRUK PEMBAYARAN JS FAMILY ---")
print("Status Member :", "Ya" if is_member else "Tidak")
print("Produk         :", nama)
print("Jumlah         :", jumlah)
print("Harga Satuan   : Rp", harga)
print("Total Belanja  : Rp", total)
print("Diskon Member  : Rp", diskon)
print("Total Bayar    : Rp", bayar)
print("\nTerima kasih telah berbelanja di JS Familly Store!") 
