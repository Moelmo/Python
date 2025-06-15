import streamlit as st

cols = st.columns(5)

if cols[0].button("Tombol 1"):
    st.write("Klik Tombol 1")

if cols[1].button("Tombol 2"):
    st.write("Klik Tombol 2")

if cols[2].button("Tombol 3"):
    st.write("Klik Tombol 3")

if cols[3].button("Tombol 4"):
    st.write("Klik Tombol 4")

if cols[4].button("Tombol 5"):
    st.write("Klik Tombol 5")


# for version

colum = st.columns(5)

for i in range(5):
    if colum[i].button(f"Tombol {i+1}"):
        st.write(f"Tombol {i+1}")