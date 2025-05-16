def simpan_user(UserName, Password):
    with open("data.txt", "a") as file:
        file.write(f"{UserName} : {Password}")

def cek_login(Username, Password):
    with open("data.txt", "r") as file:
        for baris in file:
            user, pw = baris.strip().split(":")
            if user == Username and pw == Password:
                return True
    return False



def landing(UserName):
    print("=============================")
    print(f"Welcome {UserName}")
    print("=============================")


print("Welcome Guest")
print("1. Login")
print("2. Register")

halo = input("Login Atau Register (1/2) : ")
if halo == "1":
    UserName = input("Masukkan UserName Anda : ")
    Password = input("Masukkan Password Anda : ")
    print(f"""
    ===============\n
    Username = {UserName}\n
    Password = {Password}\n
    ===============
""")
    if cek_login(UserName, Password):
        print("Login Berhasil")
        landing()
    else:
        print("Username atau password salah")
else:
    print("Keluar")