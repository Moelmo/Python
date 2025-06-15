import streamlit as st 
import random 
import time

st.title("Game")
st.header("Tebak angka 1 sampai 100")

if "angka" not in st.session_state:
    st.session_state.angka = 0
    st.session_state.angka2 = 0
    st.session_state.angka3 = 0
    st.session_state.angka4 = 0
    st.session_state.angka5 = 0 
if "attemp" not in st.session_state:
    st.session_state.attemp = 0
if "reset" not in st.session_state:
    st.session_state.reset = 0
if "benar" not in st.session_state:
    st.session_state.benar = 0
if "salah" not in st.session_state:
    st.session_state.salah = 0

def mulai():
    st.session_state.angka = random.randint(1,100)
    if st.session_state.angka < 6:
        st.session_state.awal = st.session_state.angka - 1
        st.session_state.akhir = st.session_state.angka + random.randint(1,3)
        st.session_state.angka2 = random.randint(1,5)
        st.session_state.angka3 = random.randint(1,5)
        st.session_state.angka4 = random.randint(1,5)
        st.session_state.angka5 = random.randint(1,5)
    elif st.session_state.angka < 20:
        st.session_state.awal = st.session_state.angka - random.randint(1,5)
        st.session_state.akhir = st.session_state.angka + random.randint(1,5)
        st.session_state.angka2 = random.randint(1,10)
        st.session_state.angka3 = random.randint(1,10)
        st.session_state.angka4 = random.randint(1,10)
        st.session_state.angka5 = random.randint(1,10)
    elif st.session_state.angka < 40:
        st.session_state.awal = st.session_state.angka - random.randint(1,10)
        st.session_state.akhir = st.session_state.angka + random.randint(1,10)
        st.session_state.angka3 = random.randint(1,15)
        st.session_state.angka4 = random.randint(1,15)
        st.session_state.angka5 = random.randint(1,15)
        st.session_state.angka2 = random.randint(1,15)
    else:
        st.session_state.awal = st.session_state.angka - random.randint(1,15)
        st.session_state.akhir = st.session_state.angka + random.randint(1,15)
        st.session_state.angka2 = random.randint(1,20)
        st.session_state.angka3 = random.randint(1,20)
        st.session_state.angka4 = random.randint(1,20)
        st.session_state.angka5 = random.randint(1,20)

if st.session_state.angka == 0:
    mulai()


st.write(f"{st.session_state.angka}")
st.write(f"#### Tebak angka berikut")
st.write(f"#### Clue : {st.session_state.awal} hingga {st.session_state.akhir}")

angka = st.session_state.angka
pilihan = [
    angka, 
    angka-st.session_state.angka2, 
    angka-st.session_state.angka3, 
    angka+st.session_state.angka4, 
    angka+st.session_state.angka5
    ]

if "urutan" not in st.session_state:
    random.shuffle(pilihan)
    st.session_state.urutan = pilihan

pilihan = st.session_state.urutan

cols = st.columns(5)
for i, p in enumerate(pilihan):
    if cols[i].button(str(p), key=f"pilihan_{i}"):
        if p == angka:
            st.success("Jawaban Anda Benar")
            time.sleep(1.5)
            mulai()
            st.session_state.benar += 1
            st.session_state.attemp = 0
            st.session_state.reset = 0
            del st.session_state.urutan
            st.rerun()
        elif st.session_state.reset > 1:
            st.warning("Ganti Soal...")
            mulai()
            st.session_state.salah += 1
            st.session_state.attemp += 1
            st.session_state.reset = 0
            time.sleep(1.5)
            del st.session_state.urutan
            st.rerun()
        else:
            st.error("Jawaban Anda Salah")
            st.session_state.salah += 1
            st.session_state.reset += 1
            st.session_state.attemp += 1


st.write(f"Percobaan Ke : {st.session_state.attemp}")
st.write(f"Menjawab Dengan Benar : {st.session_state.benar}")
st.write(f"Menjadwab Dengan Salah : {st.session_state.salah}")



