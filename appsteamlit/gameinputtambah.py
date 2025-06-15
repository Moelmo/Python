import streamlit as st 
import random
import time


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

st.text_input("pilih jawaban yang benar", key="jawaban")
if st.button("Submit"):
    try:
        if int(st.session_state.jawaban) == st.session_state.hasil:
            st.success("jawaban anda benar")
            soal()
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("Jawaban anda salah")
    except ValueError:
        st.warning("Masukkan input yang benar")
    

