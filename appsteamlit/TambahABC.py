import streamlit as st
import time, random

st.title("Game#2")
st.subheader("Jawab dengan benar")

# Inisialisasi session state
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
    st.session_state.attemp = 0
    st.session_state.soal = 1
    st.session_state.nilai = 0
    st.session_state.selesai = False

# Fungsi untuk memulai soal baru
def mulai():
    st.session_state.tambah_a = random.randint(1, 10)
    st.session_state.tambah_a1 = random.randint(1, 5)
    st.session_state.tambah_b = random.randint(1, 10)
    st.session_state.tambah_b1 = random.randint(1, 5)
    st.session_state.tambah_c = random.randint(1, 10)
    st.session_state.tambah_c1 = random.randint(1, 10)
    st.session_state.tambah_d = random.randint(1, 10)
    st.session_state.tambah_d1 = random.randint(1, 10)

    hasil = st.session_state.tambah_a + st.session_state.tambah_b
    salah_1 = hasil + st.session_state.tambah_a1
    salah_2 = hasil - st.session_state.tambah_b1
    salah_3 = st.session_state.tambah_c + st.session_state.tambah_c1
    salah_4 = st.session_state.tambah_d - st.session_state.tambah_d1

    pilihan = [hasil, salah_1, salah_2, salah_3, salah_4]
    random.shuffle(pilihan)

    st.session_state.pilihan = pilihan
    st.session_state.hasil = hasil

# Mulai soal pertama
if st.session_state.hasil == -1:
    mulai()

# Tampilkan soal
if not st.session_state.selesai:
    st.write(f"#### {st.session_state.tambah_a} + {st.session_state.tambah_b} = ...")

    pilihan = st.session_state.pilihan
    cols = st.columns(5)
    for i, p in enumerate(pilihan):
        if cols[i].button(str(p), key=f"pilihan{i}"):
            if p == st.session_state.hasil:
                st.success("Jawaban anda benar!")
                st.session_state.jawaban_benar += 1
                st.session_state.attemp = 0
            else:
                st.error("Jawaban anda salah!")
                st.session_state.jawaban_salah += 1
                st.session_state.attemp += 1
                if st.session_state.attemp >= 1:
                    st.warning("Sudah 1x salah, lanjut soal berikutnya.")
                    st.session_state.attemp = 0

            st.session_state.soal += 1

            if st.session_state.soal > 20:
                st.session_state.nilai = st.session_state.jawaban_benar * 5
                st.session_state.selesai = True
            else:
                time.sleep(1.5)
                mulai()
                st.rerun()

# Tampilkan hasil
if st.session_state.selesai:
    st.subheader("🎯 Hasil Akhir")
    if st.session_state.nilai < 49:
        st.error(f"Nilai Anda: {st.session_state.nilai}")
    elif st.session_state.nilai < 74:
        st.warning(f"Nilai Anda: {st.session_state.nilai}")
    else:
        st.success(f"Nilai Anda: {st.session_state.nilai}")

    # Tombol reset
    if st.button("Ulangi"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Info skor saat ini
st.markdown("---")
st.write(f"Benar/Salah : {st.session_state.jawaban_benar}/{st.session_state.jawaban_salah}")
st.write(f"Soal : {min(st.session_state.soal, 20)}/20")
