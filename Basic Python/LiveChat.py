# simple live chat
import time

# login register sistem 
def register():
    username = input("Masukkan username : ")
    password =  input("Masukkan password : ")

    with open("datauser.txt", "a") as file:
        file.write(f"{username}, {password}\n")
    print("Register Berhasil")

def login():
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    with open("datauser.txt", "r") as file:
        datauser = file.readlines()

    for user in datauser:
        saved_username, saved_password = user.strip().split(",")
        saved_username = saved_username.strip()
        saved_password = saved_password.strip()
        if username == saved_username and password == saved_password:
            print("Login Berhasil\n")
            return
    print("Login gagal. Username atau password salah.\n")

def menu():
    while True:
        print("===== Main Menu =====")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        choice = input("Pilih menu : ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Keluar")
            break
        else:
            print("masukkan input 1/2/3")

menu()