import time 

log_list = []

waktu = time.localtime()
jam = waktu.tm_hour
menit = waktu.tm_min 
detik = waktu.tm_sec 


while True:
    pesan = input("Masukkan Pesan : ")
    if pesan == "s":
        break
    timestamp = f"{jam}:{menit}:{detik}"

    log_list.append({
        "waktu": timestamp,
        "pesan": pesan 
    })
    print("\n" * 25)
    print("========================================")
    for log in log_list:
        print(f"[{log["waktu"]}]: {log["pesan"]}")
    print("========================================")
    if len(log_list) > 4:
        log_list.pop(0)