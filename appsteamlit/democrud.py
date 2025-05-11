import streamlit as st 

st.title("Simple CRUD")

if "namalist" not in st.session_state:
    st.session_state.namalist = ["Moelmo"]

if "add" not in st.session_state:
    st.session_state.add = ""

def tambah():
    new = st.session_state.add.strip()
    if new:
        st.session_state.namalist.append(new)
        st.session_state.add = ""

new = st.text_input("Masukkan nama", key="add")
st.button("Tambah", on_click=tambah)

st.subheader("Daftar Nama")
for i, nama in enumerate(st.session_state.namalist):
    st.write(f"{i}. {nama}")