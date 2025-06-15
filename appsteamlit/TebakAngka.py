import streamlit as st 
import random 
import time

st.title("Game")
st.header("Tebak angka")

if "angka" not in st.session_state:
    st.session_state.angka = 0

def mulai():
    st.session_state.angka = random.randint(1,100)

if st.session_state.angka == 0:
    mulai()

st.write(f"{st.session_state.angka}")

