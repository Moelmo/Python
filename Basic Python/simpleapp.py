import time

waktu = time.localtime()
jam = waktu.tm_hour
menit = waktu.tm_min
detik = waktu.tm_sec
hari = waktu.tm_mday
bulan = waktu.tm_mon
tahun = waktu.tm_year
timestamp = f"{jam}:{menit}:{detik}"
days = f"{hari}/{bulan}/{tahun}"

def register():
    username = input("Buat Username Anda : ")
    password = input("Buat Password Anda : ")
    with open("data_usr.txt", "a") as file:
        file.write(f"{username},{password}\n")
    with open("log_app.txt", "a") as file:
        file.write(f"[{days} | {timestamp}]: {username} Berhasil Terdaftar dalam data bese\n")
    print(f"[{days} | {timestamp}]: {username} Berhasil Terdaftar\n")
    mainmenu()

def login():
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")

    with open("data_usr.txt", "r") as file:
        for line in file:
            user, pw = line.strip().split(",")
            if user == username and pw == password:
                print(f"[{timestamp} | {days}]: {username} Berhasil Login\n\n")
                with open("log_app.txt", "a") as file:
                    file.write(f"[{days} | {timestamp}]: {username} Berhasil Login\n")
                menu(username)
                return username
    print(f"[{days} | {timestamp}]: Gagal Login {username} anda tidak terdaftar atau password salah\n")
    with open("log_app.txt", "a") as file:
        file.write(f"[{days} | {timestamp}]: {username} Gagal Login username tidak terdaftar atau password {password} salah\n")
    mainmenu()
    return None

def mainmenu():
    print("""
=====[Simple App]=====
1. Login
2. Register
\n
""")
    try:
        pilihmenu = int(input("Pilih [1/2] : "))
        if pilihmenu == 1:
            login()
        elif pilihmenu == 2:
            register()
        else:
            mainmenu()
    except ValueError:
        print("masukkan angka yang benar bukan huruf")

def persegi(username):
    try:
        luas = float(input("Masukkan Luas Persegi : "))
        hasil = luas * luas
        print(f"[{days} | {timestamp}]: Hasil {luas} x {luas} adalah {hasil}")
        with open("act_log_simpleapp.txt", "a") as file:
            file.write(f"[{days} | {timestamp}] User : {username} | Hasil : {hasil}\n")
        pilih = input("\nLanjut/Keluar [t/s] :")
        if pilih == "s":
            menu()
        elif pilih == "t":
            persegi(username)
        else:
            print("Masukkan input yang benar")

    except ValueError:
        print("Masukkan angka yang benar")
        persegi(username)


def lingkaran(username):
    try:
        r =  float(input("Masukkan jari-jari lingkaran : "))
        luas = (22/7) * r**2
        print(f"[{days} | {timestamp}]: Luas Lingkaran : {luas:.2f}")
        with open("act_log_simpleapp.txt", "a") as file:
            file.write(f"[{days} | {timestamp}] User : {username} | Hasil : {luas:.2f}\n")
        pilih = input("\nLanjut/Keluar [t/s] : ")
        if pilih == "s":
            menu()
        elif pilih == "t":
            lingkaran(username)
        else:
            print("Masukkan input yang benar")
    except ValueError:
        print("MAsukkan angka yang benar bukan huruf")
        lingkaran(username)


def cekgg(username):
    try:
        angka = int(input("Masukkan angka bebas : "))
        if angka % 2 == 0:
            print(f"[{days} | {timestamp}]: {angka} Genap")
            with open("act_log_simpleapp.txt") as file:
                file.write(f"[{days} | {timestamp}] User : {username} | Hasil {angka} Genap\n")
        else:
            print(f"[{days} | {timestamp}]: {angka} Ganjil")
            with open("act_log_simpleapp.txt") as file:
                file.write(f"[{days} | {timestamp}] User : {username} | Hasil {angka} Ganjil\n")
        print("\n")

        
        pilih = input("\nLanjut/Keluar [t/s] : ")
        if pilih == "s":
            menu()
        elif pilih == "t":
            cekgg(username)
        else:
            print("Masukkan input yang benar")

    except ValueError:
        print("Masukkan angka yang benar bukan huruf")
        cekgg(username)


            

def menu(username):
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
            print(f"[{timestamp} | {username}]: Hitung Luas Persegi")
            persegi(username)
        elif pilihmenu == 2:
            print(f"[{timestamp} | {username}]: Hitung Luas Lingkaran")
            lingkaran(username)
        elif pilihmenu == 3:
            print(f"[{timestamp} | {username}]: Cek Ganjil / Genap")
            cekgg(username)
        elif pilihmenu == 4:
            print("""
============================================
Terimakasih Sudah Menggunakan Program Moelmo
============================================
""")
            with open("act_log_simpleapp.py", "a") as file:
                file.write(f"[{days} | {timestamp}] {username} Mengakhiri program")
        else:
            print("Pilih menu berikut [1/2/3/4]")
    except ValueError:
            print("Masukkan Input Angka")
            menu()
        
mainmenu()
