bulan_berapa = int(input("Masukkan bulan ke berapa (1-12) :")) #Untuk menginput angka yang ingin di tuju

bulan = ["January", "Febuary", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober","November", "Desember"] # databulan yang ada

if 1 <= bulan_berapa <= 12: #jika 1 lebih kecil sama dengan bulan_berapa lebih kecil sama dengan 12, jika kamu menginput 0 maka kode tidak akan di eksekusi dan juga menginput angka lebih dari 12 kode juga tidak akan di eksekusi
    print("Bulan", bulan[bulan_berapa -1]) #print hasil yang akan di ekseskusi


