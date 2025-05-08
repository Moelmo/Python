import streamlit as st

st.title("Penghitung Diskon")

namab = st.text_input("Masukkan Nama Barang (Opsional) [Default = Sepatu]", value="Sepatu")
harga = st.number_input("Masukkan Harga Barang", 0)
diskon = st.number_input("Masukkan Harga Diskon(1-100)", 0)
hitung = st.button("Hitung Hasil Diskon") 

if hitung:
    if diskon >= 100:
        st.error("Kamu memasukkan harga diskon melebihi 100%")
    else:
        normal = harga
        hasil = harga * diskon/100
        hdiskon = harga - hasil
        st.write(f"Harga Normal {namab} adalah Rp.{normal} dan anda memberi diskon sebesar {diskon}% maka di potong Rp.{hasil}")
        st.write(f"Harga Normal {namab} Rp.{normal}, Harga diskon Rp.{hdiskon}")
        st.success(f"Harga {namab} Rp.{normal} Diskon Menjadi Rp.{hdiskon}")