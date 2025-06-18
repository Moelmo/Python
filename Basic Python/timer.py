import time 

mulai = time.perf_counter()
time.sleep(5)
end = time.perf_counter()
time.sleep(2)
waktu = end - mulai
print(f"{waktu:.2f}")

