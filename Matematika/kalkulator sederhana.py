# kalkulator tambah kurang kali bagi sederhana

print("==========================")
print("Kalkulator Sederhana")
print("==========================\n")

print("===========================")
print("pilih operasi yang ingin dilakukan")
print("1. Penjumlahan")
print("2. Pengurangan") 
print("3. Perkalian")
print("4. Pembagian")
print("5. Keluar")
print("==========================\n")
kalkulasi = int(input("Masukkan pilihan (1/2/3/4/5): "))
if kalkulasi == 1:
    tambah1 = int(input("Masukkan angka pertama: "))
    tambah2 = int(input("Masukkan angka kedua: "))
    hasil = tambah1 + tambah2
    print(f"Hasil penjumlahan {tambah1} + {tambah2} = {hasil}")
else:
    print("Operasi tidak valid")