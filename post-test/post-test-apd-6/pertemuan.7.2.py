try: 
   angka = int(input('masukkan harga\t: '))
except ValueError:
   print('inputan bukan berupa angka')
else:
   print(angka)

finally :
   print('komang 218')


try : 
   usn = input = input('Panjang kurang dari 5 karakter: ')
   if len(usn) < 5:
      raise ValueError('Nama minimal memiliki 5 karakter ')
except ValueError as e:
   print(e)
