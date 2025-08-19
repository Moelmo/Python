import time
import random

# random teks
words = [
    "tes", "hallo", "hai", "mouse", "ram", "pc", "monitor"
]

score = 0
duration = 30
start_time = time.time()

print("=== Typing Rush CLI ===")
print(f"Ketik sebanyak mungkin dalam {duration} detik")
print("Tekan Enter untuk mulai...")
input()

# game di mulai 
while True:
    current_time = time.time()
    elapsed = current_time - start_time
    remaining = duration - int(elapsed)

    if remaining <= 0:
        print("\nWaktu Habis")
        break

    word = random.choice(words)
    print(f"\nKetik: {word} ({remaining}s tersisa)")
    typed = input(">> ")

    if typed.strip() == word:
        score += 1
        print("Benar")
    else:
        print("Salah")

# score akhir
print(f"\nscore akhir kamu: {score}")