import sys
import time

# tels, delay
lirik = [
    ("Menangkap banyak kisah yang telah dan kan terjadi", 0.1),
    ("Tak kan slalu membuat semua orang suka", 0.09)
]

def lagu(teks, delay):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()

for baris, delay in lirik:
    lagu(baris, delay)
    time.sleep(1)