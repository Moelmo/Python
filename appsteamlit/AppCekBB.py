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

with st.expander("Cara penggunaan"):
    st.write("""Rumus BIM (Body Mass Index)
BIM mengukur proporsi berat badan dengan tinggi badan.\n""")
with st.expander("Show"):
    st.write("tes")
with st.expander("Show"):
    st.write("tes")