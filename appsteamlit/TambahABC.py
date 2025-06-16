import streamlit as st
import time, random

st.title("Game#2")
st.subheader("Jawab dengan benar")

# variable

#state variable
if "tambah" not in st.session_state:   
    st.session_state.tambah = True 
    st.session_state.tambah_a = 0 
    st.session_state.tambah_b = 0
    st.session_state.tambah_a1 = 0
    st.session_state.tambah_b1 = 0
    st.session_state.tambah_c = 0
    st.session_state.tambah_c1 = 0
    st.session_state.tambah_d = 0
    st.session_state.tambah_d1 = 0
    st.session_state.pilihan = []
    st.session_state.hasil = -1
    st.session_state.jawaban_benar = 0
    st.session_state.jawaban_salah = 0

def mulai():
    st.session_state.tambah_a = random.randint(1,10)
    st.session_state.tambah_a1 = random.randint(1,10)
    st.session_state.tambah_b = random.randint(1,10)
    st.session_state.tambah_b1 = random.randint(1,10)
    st.session_state.tambah_c = random.randint(1,10)
    st.session_state.tambah_c1 = random.randint(1,10)
    st.session_state.tambah_d = random.randint(1,10)
    st.session_state.tambah_d1 = random.randint(1,10)

    hasil = st.session_state.tambah_a + st.session_state.tambah_b
    salah_1 = hasil + st.session_state.tambah_a1
    salah_2 = hasil - st.session_state.tambah_b1
    salah_3 = st.session_state.tambah_c + st.session_state.tambah_c1
    salah_4 = st.session_state.tambah_d - st.session_state.tambah_d1

    pilihan = [hasil, salah_1, salah_2, salah_3, salah_4]
    random.shuffle(pilihan)

    st.session_state.pilihan = pilihan
    st.session_state.hasil = hasil

if st.session_state.hasil == -1:
    mulai()


st.write(f"{st.session_state.tambah_a} + {st.session_state.tambah_b} = ...")

# st.write(f"{st.session_state.tambah_a} + {st.session_state.tambah_b} = ...")

pilihan = st.session_state.pilihan
cols = st.columns(5)
for i, p in enumerate(pilihan):
    if cols[i].button(str(p), key=f"pilihan{i}"):
        if p == st.session_state.hasil:
            st.success(f"Jawaban anda benar {st.session_state.tambah_a} + {st.session_state.tambah_b} = {st.session_state.hasil}")
            time.sleep(1.5)
            mulai()
            st.rerun()
        else:
            st.error("Jawaban anda salah")

st.markdown("---")