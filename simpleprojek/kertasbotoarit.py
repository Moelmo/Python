import random

while True:
    isi = ["Kertas", "Batu", "Gunting"]
    p = isi.copy()
    Com = random.choice(isi)

    print("Game Kertas Batu Gunting")
    print("1. Kertas\n2. Batu\n3. Gunting\n4. Keluar")
    try:
        pilih = int(input("Pilih 1/2/3/4 : "))
        if pilih == 4:
            print("Terimakasih sudah bermain")
            break
        if pilih not in [1,2,3]:
            print("Pilihan tidak valid")
            continue

        ph = (p[pilih - 1])
        print(f"\nPlayer memilih : {ph}")
        print(f"Computer memilih : {Com}")

        if ph == Com:
            print("Hasilnya : Seri\n")
        elif (ph == "Kertas" and Com == "Batu") or (ph == "Batu" and Com == "Gunting") or (ph == "Gunting" and Com == "Kertas"):
            print("Player Menang\n")
        else:
            print("Computer Menang\n")


    except ValueError:
            print("Masukkan input yang benar\n\n")
