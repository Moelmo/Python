import streamlit as st 

st.title("To Do List")

if "list" not in st.session_state:
    st.session_state.list = []

task = st.text_input("Masukkan Tugas")
if st.button("Tambah") and task:
    st.session_state.list.append({"Teks" : task, "Done" : False})
    st.success(f"Tugas {task} Berhasil di tambah")

st.subheader("List")
for i, todo in enumerate(st.session_state.list):
    done = st.checkbox(todo["Teks"], value=todo["Done"], key=i)
    st.session_state.list[i]["Done"] = done

if st.button("Hapus semua tugas selesai"):
    st.session_state.list = [t for t in st.session_state.list if not t["Done"]]
    st.success("Tugas selesai di hapus")
    st.rerun()