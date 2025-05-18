# simple live chat
import time


chatlist = []

#chattlog sistem
def save_chatlog():
    with open("chatlog.txt", "w") as file:
        for message in chatlist:
            file.write(f"{message['waktu']}, {message['username']}, {message['pesan']}\n")

def load_chatlog():
    try:
        with open("chatlog.txt", "r") as file:
            lines = file.readline()
            for line in lines:
                parts = line.strip().split(", ", 2)
                if len(parts) == 3:
                    chatlist.append({
                        "waktu" : parts[0],
                        "username" : parts[1],
                        "pesan" : parts[2]           
                        })
    except FileNotFoundError:
        open("chatlog.txt", "w").close()

#live chat sitem

def livechat(username):
    while True:
        pesan = input("Masukkan pesan : ")
        if pesan.lower() == "s":
            save_chatlog()
            menu()
            break

        waktu = time.localtime()
        timetamp = f"{waktu.tm_hour}:{waktu.tm_min}:{waktu.tm_sec}"

        chatlist.append({
            "waktu" : timetamp,
            "username" : username,
            "pesan" : pesan
        })

        #display chat
        print("\n" * 25)
        print("==========================================")
        for log in chatlist:
            print(f"[{log["waktu"]}][{log["username"]}]: {log["pesan"]}")
        print("==========================================")

        #batas chat
        if len(chatlist) > 14:
            chatlist.pop(0)


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
            livechat(username)
            return
    print("Login gagal. Username atau password salah.\n")

def menu():
    load_chatlog()
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
            save_chatlog()
            print("Keluar")
            break
        else:
            print("masukkan input 1/2/3")



if __name__ == "__main__":
    menu()