import random
import time

benar = 0
salah = 0
jawaban = 0
start = time.time()

while True:
    a = random.randint(1,10)
    b = random.randint(1,10)
    h = a + b
    try:
        if jawaban == 10:
            print(f"Hasil score kamu Benar/Salah : {benar}/{salah}")
            end = time.time()
            durasi = end - start
            print(f"Waktu mengerjakan anda adalah : {round(durasi,2)} detik")
            break
        print("\nSilahkan jawab")
        jawab = int(input(f"{a} + {b} = "))
        if h == jawab:
            print(f"{a} + {b} = {jawab}")
            print(f"Jawaban mu benar {h}")
            benar += 1
            jawaban += 1
        else:
            print(f"Jawaban mu salah seharusnya {h}")
            print(f"{a} + {b} = {jawab}")
            jawaban += 1
            salah += 1
    except ValueError:
        print("Masukkan Angka Bukan Huruf")
