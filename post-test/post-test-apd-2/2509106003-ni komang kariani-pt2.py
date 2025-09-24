# Program untuk cek berat badan di layanan kesehatan Daffa yang berguna untuk menentukan berat badan ideal
print("=" * 75)
print("|                         LAYANAN KESEHATAN DASAR DAFFA                             |")
print("|                           PROGRAM CEK BERAT BADAN                                 |")
print("=" * 75)

# Meminta data pasien dari pengguna
nama_pasien = input("Masukkan Nama Pasien: ")
tinggi_badan = float(input("Masukkan Tinggi Badan (cm): "))
berat_badan = float(input("Masukkan Berat Badan (kg): "))

#penentuan untuk tolak ukurnya
berat_ideal = tinggi_badan - 100
is_kelebihan = berat_badan > berat_ideal
is_kekurangan = berat_badan < (berat_ideal - 10)

# Kekurangan = 0, Kelebihan = 2, Ideal = 1
kategori_berat = int(is_kelebihan) * 2 + int(not is_kekurangan and not is_kelebihan) * 1

# Daftar status: kekurangan, ideal, atau kelebihan
status_list = ["Kekurangan Berat Badan", "Berat Badan Ideal", "Kelebihan Berat Badan"]

#keterangan statusnya
status = status_list[kategori_berat]

print("-" * 85)
print("|                               HASIL CEK BERAT BADAN                               |")
print("-" * 85)
print(f"| Nama Pasien     : {nama_pasien:<53}            |")
print(f"| Tinggi Badan    : {tinggi_badan:<5.1f} cm{' ' * 153}    |")
print(f"| Berat Badan     : {berat_badan:<5.1f} kg{' ' * 40}    |") 
print(f"| Berat Ideal     : {berat_ideal:<5.1f} kg{' ' * 53}    |")
print(f"| Status          : {status:<53}            |")
print("-" * 85)

print("\nTerima kasih telah menggunakan layanan kesehatan Daffa!")