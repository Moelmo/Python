import random

#tebak tebakan angka

angka = random.randint(1,10)

while True:
    tebak =  int(input("Tebak angka dari 1 hingga 10 : "))
    try:
        if tebak == angka:
            print(f"Kamu benar angka yang kamu tebak adalah {angka}")
            break
        else:
            print("Jawaban salah")
    except ValueError:
        print("Masukkan input angka")