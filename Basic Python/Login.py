def register():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registrasi berhasil\n")

def login():
    username = input("Masukkan username :")
    password = input("Masukkan password :")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        saved_username, saved_password = user.strip().split(",")
        if username == saved_username and password == saved_password:
            print("Login Berhasil\n")
            return
    print("Login gagal. Username atau password salah.\n")

def menu():
    while True:
        print("===== Menu =====")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Keluar")
            break
        else:
            print("Input Tidak Valid")

menu()