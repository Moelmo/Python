import random

scorep = 0
scoreb = 0

while True:
    isi = ["Kertas", "Batu", "Gunting"]
    p = isi.copy()
    Com = random.choice(isi)

    print("Game Kertas Batu Gunting")
    print("1. Kertas\n2. Batu\n3. Gunting\n4. Keluar")
    try:
        pilih = int(input("Pilih 1/2/3/4 : "))
        if pilih == 4:
            print("\n\n\nTerimakasih sudah bermain")
            print(f"Score Player/Computer : {scorep}/{scoreb}")
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
            scorep += 1
        else:
            print("Computer Menang\n")
            scoreb += 1


    except ValueError:
            print("Masukkan input yang benar\n\n")
