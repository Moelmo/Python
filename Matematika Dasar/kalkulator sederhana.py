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
while True:
    kalkulasi = int(input("Masukkan pilihan (1/2/3/4/5): "))
    if kalkulasi == 1:
        tambah1 = int(input("Masukkan angka pertama: "))
        tambah2 = int(input("Masukkan angka kedua: "))
        hasil = tambah1 + tambah2
        print(f"Hasil penjumlahan {tambah1} + {tambah2} = {hasil}")
    elif kalkulasi == 2:
        kurang1 = int(input("Masukkan angka pertama: "))
        kurang2 = int(input("Masukkan angka kedua: "))
        hasil == kurang1 - kurang2
        print(f"Hasil pengurangan {kurang1} - {kurang2} = {hasil}")
    elif kalkulasi == 3:
        kali1 = int(input("Masukkan angka pertama: "))
        kali2 = int(input("Masukkan angka kedua: "))
        hasil = kali1 * kali2
        print(f"Hasil perkalian {kali1} * {kali2} = {hasil}")
    elif kalkulasi == 4:
        bagi1 = int(input("Masukkan angka pertama: "))
        bagi2 = int(input("Masukkan angka kedua: "))
        if bagi2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan")
        else:
            hasil = bagi1 / bagi2
            print(f"Hasil pembagian {bagi1} / {bagi2} = {hasil}")

    else:
        print("Masukkan input yang benar")