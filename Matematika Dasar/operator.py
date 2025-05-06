umur = 15
punya_ktp = False

# penggunaan operator logika
# operator and

if umur >= 17 and punya_ktp:
    print("Bisa membuat SIM")
else:
    print("Tidak bisa membuat SIM")

# penggunakan operator or

izin = False
if umur >= 17 or izin:
    print("Bisa membuat SIM")
else:
    print("Tidak bisa membuat SIM")


# penggunaan operator not
if not punya_ktp:
    print("Tidak bisa membuat SIM")
else:
    print("Bisa membuat SIM")

#penjelasan singkat mengenai operator logika

#penjelsan singkat mengenai operator AND (dan)
# jika keduanya bernilai True maka jawabnya True, jika salah satu dari nilai A dan B itu False maka jawabnya false, jadi AND itu mengambil nilai A dan B yang bersifat True harus keduanya True tidadk boleh ada yan salah satunya false


# penjelasan singkat mengenail operator OR (atau)
# jiak salah satu dari nilai A dan B itu true maka jawabanya true tapi jika keudanya false maka jawabanya juga false, tapi jika salah satunya true maka jawabanya true, jadi OR itu mengambil salah satu dari nilai A dan B yang bersifat True

# penjelasan singkat mengenai operator NOT (tidak)
# jika nilai A itu True maka jawabanya False, jika nilai A itu False maka jawabanya True, jadi NOT itu membalikkan nilai dari A, jika A itu True maka jawabanya False dan sebaliknya

# contohnya if not punya_ktp: print(jaweban), artinya jika tidak punya ktp maka jawabanya false atau kebalikannya