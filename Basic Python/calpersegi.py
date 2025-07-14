spas = "\n"

def persegi():
    try:
        luas = float(input("Masukkan Luas Persegi : "))

        hasil = luas * luas
        print(f"Hasil {luas} x {luas} adalah {hasil}")

        print("Ulangi/Keluar [1/2]")

        pilihmenu = int(input("Pilih menu : "))
        if pilihmenu == 1:
            print(spas)
            persegi()
        elif pilihmenu == 2:
            main()
        else:
            print("pilih menu berikut [1/2]")
    except ValueError:
        print("Masukkan angka yang benar 1 atau 2")
        persegi()

def lingkaran():
    try:
        r = float(input("Masukkan jari-jari lingkaran :"))

        luas = (22/7) * r**2
        print(f"Luas Lingkaran : {luas:.2f}")

        print("Ulangi/Keluar [1/2]")
        pilihmenu = int(input("Pilih menu : "))
        if pilihmenu == 1:
            print(spas)
            lingkaran()
        elif pilihmenu == 2:
            main()
        else:
            print("Pilih menu berikut [1/2]")
    except ValueError:
        print("Masukkan angka yang benar bukan huruf")
        lingkaran()

def cekgg():
    try:
        angka = int(input("Masukkan angka bebas : "))
        if angka % 2 == 0:
            print(f"{angka} Genap")
        else:
            print(f"{angka} Ganjil")

        print("Ulangi/Keluar [1/2]")
        pilihmenu = int(input("Pilih menu : "))
        if pilihmenu == 1:
            print(spas)
            cekgg()
        elif pilihmenu == 2:
            main()
        else:
            print("Pilih menu berikut [1/2]")
    except ValueError:
        print("Masukkan angka yang benar bukan huruf")
        cekgg()

def main():
    print("""
=== Menu Program Sederhana ===
1. Hitung Luas Persegi
2. Hitung Luas Lingkaran
3. Cek Ganjil / Genap
4. Keluar
""")
    try:
        pilihmenu = int(input("Pilih [1/2/3/4] : "))
        if pilihmenu == 1:
            print("Hitung Luas Persegi")
            persegi()
        elif pilihmenu == 2:
            print("Hitung Luas Lingkaran")
            lingkaran()
        elif pilihmenu == 3:
            print("Cek Ganjil / Genap")
            cekgg()
        elif pilihmenu == 4:
            print("""
============================================
Terimakasih Sudah Menggunakan Program Moelmo
============================================
""")
        else:
            print("Pilih menu berikut [1/2/3/4]")
    except ValueError:
            print("Masukkan Input Angka")
            main()

main()