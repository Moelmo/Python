# kalkulator tambah kurang kali bagi sederhana
kalkulasi = 0

print("==========================")
print("Kalkulator Sederhana")
print("==========================\n")

print("===========================")
print("pilih operasi yang ingin dilakukan")
print("1. Penjumlahan")
print("2. Pengurangan") 
print("3. Perkalian")
print("4. Pembagian")
print("5. Sisa Pembagian")
print("6. Semua Operasi Perbandingan")
print("9. Keluar")
print("==========================\n")
while kalkulasi != 9:
    kalkulasi = (input("Masukkan pilihan (1/2/3/4/5/6/9): "))
    if kalkulasi == "1":
        try:
            tambah1 = int(input("Masukkan angka pertama: "))
            tambah2 = int(input("Masukkan angka kedua: "))
            hasil = tambah1 + tambah2
            print(f"Hasil penjumlahan {tambah1} + {tambah2} = {hasil}")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka")
    elif kalkulasi == "2":
        try:
            kurang1 = int(input("Masukkan angka pertama: "))
            kurang2 = int(input("Masukkan angka kedua: "))
            hasil = kurang1 - kurang2
            print(f"Hasil pengurangan {kurang1} - {kurang2} = {hasil}")
        except ValueError:
            print("Input tidak valid, silakan masukkan angka")
    elif kalkulasi == "3":
        try:
            kali1 = int(input("Masukkan angka pertama: "))
            kali2 = int(input("Masukkan angka kedua: "))
            hasil = kali1 * kali2
            print(f"Hasil perkalian {kali1} * {kali2} = {hasil}")
        except ValueError:
            print("input tidak valid, silahkan masukkan angka")
    elif kalkulasi == "4":
        try:
            bagi1 = int(input("Masukkan angka pertama: "))
            bagi2 = int(input("Masukkan angka kedua: "))
            if bagi2 == 0:
                print("Pembagian dengan nol tidak diperbolehkan")
            else:
                hasil = bagi1 / bagi2
                print(f"Hasil pembagian {bagi1} / {bagi2} = {hasil}")
        except ValueError:
            print("input tidak valid, silahkan masukkan angka")
    elif kalkulasi == "5":
        try:
            sisa1 = int(input("Masukkan angka pertama: "))
            sisa2 = int(input("Masukkan angka kedua: "))
            if sisa2 == 0:
                print("Pembagian dengan nol tidak diperbolehkan")
            else:
                hasil = sisa1 % sisa2
                print(f"Hasil sisa pembagian {sisa1} % {sisa2} = {hasil}")
        except ValueError:
            print("input tidak valid, silahkan masukkan angka")
    elif kalkulasi == "6":
        try:
            angka1 = int(input("Masukkan angka pertama: "))
            angka2 = int(input("Masukkan angka kedua: "))
            lebih_besar = angka1 > angka2
            lebih_kecil = angka1 < angka2
            sama_dengan = angka1 == angka2
            tidak_sama = angka1 != angka2
            lebihb_sama = angka1 >= angka2
            lebihk_sama = angka1 <= angka2
            print("==========================")
            print("Operasi Perbandingan")
            print("===== | lebih besar | =====")
            print(f"angka {angka1} lebih besar dari {angka2} : {angka1} > {angka2} = {lebih_besar}")
            print(f"angka {angka1} lebih besar sama dari {angka2} : {angka1} >= {angka2} = {lebihb_sama}")
            print("===== | lebih kecil | =====")
            print(f"angka {angka1} lebih kecil dari {angka2} : {angka1} < {angka2} = {lebih_kecil}")
            print(f"angka {angka1} lebih kecil sama dari {angka2} : {angka1} <= {angka2} = {lebihk_sama}")
            print("===== | sama dengan | =====")
            print(f"angka {angka1} sama dengan {angka2} : {angka1} == {angka2} = {sama_dengan}")
            print(f"angka {angka1} tidak sama dengan {angka2} : {angka1} != {angka2} = {tidak_sama}")
            print("==========================")
        except ValueError:
            print("input tidak valid, silahkan makukkan angka")

    elif kalkulasi == "9":
        print("Terima kasih telah menggunakan kalkulator sederhana")
        break
    else:
        print("Masukkan input yang benar")