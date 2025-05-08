# progam pengitung diskon

harga = int(input("Masukkan Harga Barang berapa RP."))
diskon = int(input("Masukkan diskon barang nya:(1-100)"))

normal = harga
hasil = harga * diskon/100
hdiskon = harga - hasil

print(f"harga barang Rp.{harga}, Mendapatkan diskon sebesar {diskon}%")
print(f"Harga Normal Rp.{normal}, harga Diskon {hasil}")
print(f"Uang yang harus di bayar sekarang adalah {hdiskon}")