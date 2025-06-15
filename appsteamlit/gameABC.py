import streamlit as st 
import random


if "soal" not in st.session_state:
    st.session_state.soal = (0,0)
if "hasil" not in st.session_state:
    st.session_state.hasil = 0

def soal():
    a = random.randint(1,10)
    b = random.randint(1,10)
    st.session_state.hasil = a + b
    st.session_state.soal = (a, b)

st.title("Game")
st.subheader("Tantangan hitungan cepat")

if st.session_state.soal == (0,0):
    soal()

a, b = st.session_state.soal
st.write(f"#### Soal : {a} + {b} = ...")

jawaban = st.text_input("pilih jawaban yang benar")
if st.button("Submit"):
    try:
        if int(jawaban) == st.session_state.hasil:
            st.success("jawaban anda benar")
            soal()
            st.rerun()
        else:
            st.error("Jawaban anda salah")
    except ValueError:
        st.warning("Masukkan input yang benar")

