# progam pengitung diskon

harga = int(input("Masukkan Harga Barang berapa RP."))
diskon = int(input("Masukkan diskon barang nya:(1-100)"))

hasil = harga * diskon/100

print(f"harga barang RP.{harga}, Mendapatkan diskon sebesar {diskon}%")
print(f"Harga Normal {harga}, harga Diskon {hasil}")