# rumus
# Broca
# pria = berat ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.10)
# wanita = berat ideal = (tinggi_cm - 100) - ((tinggi_cm - 100 * 0.15))

# BMI (Body Mass Index)
# < 18.15 "kurus"
# < 25 "ideal"
# < 30 "Kelebihan berat"
# 30+ "obesitas" 


import streamlit as st 

st.markdown("""
    <style>
    .rainbow-text {
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(
            90deg,
            red,
            orange,
            yellow,
            green,
            cyan,
            blue,
            violet
        );
        background-size: 400% 100%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow 5s linear infinite;
        text-align: center;
    }

    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    </style>
    <div class="rainbow-text">Cek Ideal Berat Badanmu</div>

            """,
        unsafe_allow_html=True
)

st.markdown("""---""")

with st.expander("Cara penggunaan"):
    st.write("""Rumus BIM (Body Mass Index)
BIM mengukur proporsi berat badan dengan tinggi badan.\nRumus Broca (Ideal Body Weight)
Broca menghitung berat badan ideal berdasarkan tinggi""")
with st.expander("BIM"):
    st.write("""

    ✅ Cara Menggunakan Rumus BIM
Ukur berat badan dalam kilogram (kg).
Contoh: 60 kg

Ukur tinggi badan dalam meter (m).
Contoh: 1,65 m

Masukkan ke rumus:

BIM = Berat / (Tinggi x Tinggi)
BIM = 60 / (1,65 x 1,65) = 22,04
Lihat kategori berat badan:

< 18,5 = Kurus

18,5–24,9 = Normal

25–29,9 = Gemuk

≥ 30 = Obesitas

""")
with st.expander("Broca"):
    st.write("""

✅ Cara Menggunakan Rumus Broca
Ukur tinggi badan dalam cm.
Contoh: 160 cm

Gunakan rumus sesuai jenis kelamin:

Pria:
(Tinggi - 100) - 10% dari hasil
= (160 - 100) - 10% = 60 - 6 = 54 kg

Wanita:
(Tinggi - 100) - 15% dari hasil
= (160 - 100) - 15% = 60 - 9 = 51 kg

Hasil = berat badan ideal.
""")
    
st.markdown("""---""")
    
