import streamlit as st 
from datetime import datetime

# judul aplikasi 
st.title("Aplikasi TopUp Pulsa")

# Masukkan nomor yang ingin di topup kan
phone_number = st.text_input("Masukkan Nomor Handphone Anda (+6285712345678)")

# toptup berapa
amount = st.selectbox("Ingin Top-Up Berapa", ["5000", "10000", "15000", "20000", "25000"])

# konfirmasi pembeian
if st.button("Top-Up Sekarang"):
    if phone_number.strip() == "":
        st.error("Harap masukkan nomor yang benar")
    else:
        # simulasi proses topup
        st.success(f"✅ Top-Up Sebesar Rp {amount} ke {phone_number} Berhasil")
        st.info(f"⌚ Waktu Transaksi: {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}")