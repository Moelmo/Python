import time

print("Mulai stopwatch...")

start = time.time()

# misalnya kita tunggu 3 detik
time.sleep(3)

end = time.time()
durasi = end - start

print(f"Waktu berlalu: {round(durasi, 2)} detik")

print(durasi)

