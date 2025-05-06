# konverter bilangan desimal ke biner, oktal, dan heksadesimal

print("##########################################")
print("###### Kalkulator Koversi Bilangan #######")
print("##########################################\n")

while True:
    print("####### Menu Kalkulator Konversi Bilangan #######")
    print("1. Masuk ke kalkulator konversi bilangan")
    print("2. Keluar dari kalkulator konversi bilangan")
    print("#################################################")

    konversi = input("Pilih menuu (1/2): ")
    if konversi == "1":
        try:
            angka = int(input("Masukkan bilangan desimal: "))
            if angka < 0:
                print("Bilangan harus positif.")
                break
            else:
                print("##########################################")
                print("Bilangan Desimal adalah : ", angka)
                print("Bilangan Biner adalah : ", bin(angka)[2:])
                print("Bilangan oktal adalah : ", oct(angka)[2:])
                print("Bilangan Heksadesimal adalah : ", hex(angka)[2:])
                print("##########################################")
            
        except ValueError:
            print("Input tidak valid. Silakan masukkan bilangan bulat positif.")
    elif konversi == "2":
        print("Terima kasih telah menggunakan kalkulator konversi bilangan.")
        break


# versi simple

a = int(input("Masukkan angka : "))
print(f"Bilangan Desimal      : {a}")
print(f"Bilangan Biner        :", bin(a)[2:])
print(f"Bilangan Oktal        :", oct(a)[2:])
print(f"Bilangan Heksadesimal :", hex(a)[2:])