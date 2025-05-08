import streamlit as st

st.title("Penghitung Diskon")

namab = st.text_input("Masukkan Nama Barang (Opsional) [Default = Sepatu]", value="Sepatu")
harga = st.number_input("Masukkan Harga Barang", 0)
diskon = st.number_input("Masukkan Harga Diskon(1-100)", 0)
hitung = st.button("Hitung Hasil Diskon") 

if hitung:
    if diskon >= 101:
        st.error("Kamu memasukkan harga diskon melebihi 100%")
    else:
        normal = harga
        hasil = harga * diskon/100
        hdiskon = harga - hasil
        st.write(f"Harga Normal {namab} adalah Rp.{normal} dan anda memberi diskon sebesar {diskon}% maka di potong Rp.{hasil}")
        st.write(f"Harga Normal {namab} Rp.{normal}, Harga diskon Rp.{hdiskon}")
        st.success(f"Harga {namab} Rp.{normal} Diskon Menjadi Rp.{hdiskon}")




st.markdown("""
    <div style="text-align: center; font-size: 25px; color: #555;">
        <p>Follow us on:</p>
        <a href="https://github.com" target="https://github.com/Moelmo" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/5968/5968866.png" width="35" height="35" alt="GitHub" />
        </a>
        <a href="https://discord.com" target="https://discord.users/" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111370.png" width="35" height="35" alt="Discord" />
        </a>
        <a href="https://www.tiktok.com" target="https://tiktok.com/@moelmo57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/4782/4782345.png" width="35" height="35" alt="TikTok" />
        </a>
        <a href="https://www.instagram.com" target="https://instagram.com/moelmo.57" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2111/2111463.png" width="35" height="35" alt="Instagram" />
        </a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 25px; color: #888;'>© Moelmo 2025</p>", unsafe_allow_html=True)