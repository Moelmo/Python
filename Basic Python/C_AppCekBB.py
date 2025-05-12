# rumus
# Broca
# pria = berat ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.10)
# wanita = berat ideal = (tinggi_cm - 100) - ((tinggi_cm - 100 * 0.15))

# BMI (Body Mass Index)
# < 18.15 "kurus"
# < 25 "ideal"
# < 30 "Kelebihan berat"
# 30+ "obesitas" 


def broca():
    while True:
        try: 
            tinggi_broca = int(input("Masukkan tinggi badan anda : "))
            if tinggi_broca >= 150:
                print(f"Tinggi badan anda adalah {tinggi_broca}")
                break
            else:
                print("Minimal tinggi badan 150")
        except ValueError:
            print("Masukkan input dengan angka")

    print("\n1. Laki-Laki | 2. Wanita | 3.Keluar")
    gender = input("Pilih jenis kelamin anda (1/2/3) : ")
    if gender == "1":
        gender = "Laki-Laki"
        hasil_broca = (tinggi_broca - 100) - ((tinggi_broca - 100) * 0.10)
    elif gender == "2":
        gender = "Perempuan"
        hasil_broca = (tinggi_broca - 100) - ((tinggi_broca - 100) * 0.15)
    elif gender == "3":
        main()
    else:
        print("Masukkan input dengan benar")
    
    print(f"Jenis kelamin anda adalah {gender}\n")



    print("\n" * 25) #mengkosongkan terminal
    print("########## Hasil ##########")
    print(f"Tinggi Badan : {tinggi_broca}")
    print(f"Jenis Kelamin anda : {gender}")
    print(f"Berat badan ideal anda adalah : {hasil_broca}.KG")

def bim():
    while True:
        try:
            tinggi_bim = int(input("Masukkan tinggi badan anda : "))
            print(f"Tinggi badan anda : {tinggi_bim}.cm")
            break
        except ValueError:
            print("Masukkan angka dengan benar")
        
    while True:
        try:
            berat_bim = int(input("Masukkan berat badan anda : "))
            print(f"Berat badan anda : {berat_bim}.Kg")
            break
        except ValueError:
            print("Masukkan angka dengan benar")

    tinggi_bim_m = tinggi_bim / 100
    bim = berat_bim / tinggi_bim_m ** 2
    if bim < 18.5:
        hasil_bim = "kurus"
    elif 18.5 <= bim < 25:
        hasil_bim = "Ideal"
    elif 25 <= bim < 30:
        hasil_bim = "Kelebihan Berat"
    else: 
        hasil_bim = "Obesitas"

    print("\n" * 25)
    print("########## Hasil ##########")
    print(f" Tinggi Badan Anda : {tinggi_bim}")
    print(f" Berat Badan Anda : {berat_bim}")
    print(f" Hasil Badan Anda : {hasil_bim}")


def main():

    pilih_rumus = 0
    while pilih_rumus != 3:
        print("\n" * 5)
        print("Pengecek seberapa idealnya berat badan anda")
        print("1. Rumus Broca (Khusus orang dewasa!!, hanya memasukan tinggi badan anda)")
        print("2. Rumus BMI (masukkan berat badan dan tinggi badan anda)")
        print("3. Keluar \n")
        pilih_rumus = input("Pilih rumus yang anda ingin kamu coba (1/2/3) : ")
        if pilih_rumus == "1":
            broca()
        elif pilih_rumus == "2":
            bim()
        elif pilih_rumus== "3":
            print("Terimakasih sudah menggunakan progam kami")
            break
        else:
            print("Masukkan input yang benar")

mulai = input("ketik 's' untuk memulai : ")
if mulai == "s":
    print("\n" * 25)
    main()
else:
    print("Keluar")