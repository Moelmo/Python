# semua aritmatika dasar
# penjumlahan, pengurangan, perkalian, pembagian, modulus, pangkat

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

penjumlahan = angka1 + angka2 #penjumlahan adalah operasi penambahan dua angka contoh 1+2=3
pengurangan = angka1 - angka2 #pengurangan adalah operasi pengurangan dua angka contoh 2-1=1
perkalian = angka1 * angka2 #perkalian adalah operasi perkalian dua angka contoh 2*3=6
pembagian = angka1 / angka2 #pembagian adalah operasi pembagian dua angka  contoh 6/2=3
modulus = angka1 % angka2  #modulus adalah operasi sisa bagi dua angka contoh 7%3=1
pangkat = angka1 ** angka2  #pangkat adalah operasi perpangkatan dua angka contoh 2**3=8
print("=================================")
print(f"angka yang di masukkan {angka1} dan {angka2}")
print(f"Penjumlahan: {penjumlahan}")
print(f"Pengurangan: {pengurangan}")
print(f"Perkalian: {perkalian}")
print(f"Pembagian: {pembagian}")
print(f"Modulus: {modulus}")
print(f"Pangkat: {pangkat}")
print("=================================\n")
print("Operasi Perbandingan")
lebih_besar = angka1 > angka2 #lebih besar adalah operasi perbandingan dua angka apakah angka1 lebih besar dari angka2 contoh 2>1= True
lebih_kecil = angka1 < angka2 #lebih kecil adalah operasi perbandingan dua angka apakah angka1 lebih kecil dari angka2 contoh 1<2= True
lebih_sama = angka1 == angka2 #lebih sama adalah operasi perbandingan dua angka apakah angka1 sama dengan angka2 contoh 1==1= True
lebih_tidak_sama = angka1 != angka2 #lebih tidak sama adalah operasi perbandingan dua angka apakah angka1 tidak sama dengan angka2 contoh 1!=2= True
lebih_besar_sama = angka1 >= angka2 #lebih besar sama adalah operasi perbandingan dua angka apakah angka1 lebih besar sama dengan angka2 contoh 2>=1= True
lebih_kecil_sama = angka1 <= angka2 #lebih kecil sama adalah operasi perbandingan dua angka apakah angka1 lebih kecil sama dengan angka2 contoh 1<=2= True
print("=================================")
print(f"angka {angka1} lebih besar dari {angka2} : {lebih_besar}")
print(f"angka {angka1} lebih kecil dari {angka2} : {lebih_kecil}")
print(f"angka {angka1} lebih sama dari {angka2} : {lebih_sama}")
print(f"angka {angka1} lebih tidak sama dari {angka2} : {lebih_tidak_sama}")
print(f"angka {angka1} lebih besar sama dari {angka2} : {lebih_besar_sama}")    
print(f"angka {angka1} lebih kecil sama dari {angka2} : {lebih_kecil_sama}")
print("=================================")
