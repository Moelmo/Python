def register():
    username = input("Buat Username Anda : ")
    password = input("Buat Password Anda : ")

    with open("data_user.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print(f"{username} Berhasil Terdaftar\n")
    menu()

def login():
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan Password Anda : ")

    with open("data_user.txt", "r") as file:
        for line in file:
            user, pw = line.strip().split(",")
            if user == username and pw == password:
                print(f"{username} Berhasil Login")
                return
    print(f"Gagal login {username} anda tidak terdaftar atau password salah")
    menu()


def menu():
    print("""
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
            print("Pilih menu [1/2]")
    except ValueError:
        print("masukkan angka yang benar bukan huruf")
        menu()
    
menu()