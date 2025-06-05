# import streamlit as st
# import sqlite3
# from datetime import datetime

# st.title("LiveChat Online")

# menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

import streamlit as st
import sqlite3
from datetime import datetime
import os

# --- SETUP DATABASE ---
def init_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS chat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        message TEXT,
        timestamp TEXT
    )""")
    conn.commit()
    conn.close()

# --- FUNGSI DATABASE ---
def register_user(username, password):
    try:
        conn = sqlite3.connect("chat.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def save_message(username, message):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%H:%M:%S")
    c.execute("INSERT INTO chat (username, message, timestamp) VALUES (?, ?, ?)", (username, message, timestamp))
    conn.commit()
    conn.close()

def get_messages(limit=100):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("SELECT id, username, message, timestamp FROM chat ORDER BY id DESC LIMIT ?", (limit,))
    messages = c.fetchall()
    conn.close()
    return messages[::-1]

def delete_message(message_id):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("DELETE FROM chat WHERE id=?", (message_id,))
    conn.commit()
    conn.close()

# --- SETUP ---
init_db()
st.set_page_config("Live Chat", layout="centered")
st.title("💬 Live Chat App")

# --- SESSION STATE ---
if "username" not in st.session_state:
    st.session_state.username = None
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# --- AUTH ---
if st.session_state.username:
    st.success(f"Login sebagai: {st.session_state.username}")
    if st.button("🔓 Logout"):
        st.session_state.username = None
        st.experimental_rerun()

    # --- INPUT PESAN ---
    st.markdown("---")
    st.subheader("💬 Kirim Pesan")

    chat_input = st.text_input("Tulis pesan dan tekan Enter ✨", key="chat_input")
    if st.button("Kirim") or chat_input:
        if chat_input.strip():
            save_message(st.session_state.username, chat_input.strip())
            st.experimental_rerun()

    # --- TAMPILKAN PESAN ---
    st.markdown("## 🧾 Riwayat Chat")
    messages = get_messages()

    for msg_id, user, message, timestamp in messages:
        st.markdown(f"""
        <div style='padding:6px; margin:4px 0; border-radius:8px; background:#f0f2f6'>
        <b>[{timestamp}] {user}</b>: {message}
        {"<span style='float:right'><button onclick=\"window.location.href='?del=" + str(msg_id) + "'\">🗑️</button></span>" if st.session_state.is_admin else ""}
        </div>
        """, unsafe_allow_html=True)

    # --- HAPUS PESAN (Admin) ---
    if "del" in st.experimental_get_query_params():
        msg_id = int(st.experimental_get_query_params()["del"][0])
        delete_message(msg_id)
        st.experimental_set_query_params()
        st.experimental_rerun()

else:
    menu = st.sidebar.radio("Menu", ["Login", "Register"])

    if menu == "Register":
        st.subheader("📝 Daftar")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Buat Akun"):
            if user and pwd:
                if register_user(user, pwd):
                    st.success("Berhasil daftar. Silakan login.")
                else:
                    st.error("Username sudah dipakai.")
            else:
                st.warning("Lengkapi semua kolom.")

    elif menu == "Login":
        st.subheader("🔐 Masuk")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if login_user(user, pwd):
                st.session_state.username = user
                st.session_state.is_admin = user == "admin"
                st.success("Login berhasil!")
                st.experimental_rerun()
            else:
                st.error("Login gagal. Coba lagi.")

# --- BACKUP OTOMATIS KE GOOGLE DRIVE? ---
# (Opsional - akan dijelaskan di bawah jika kamu mau)
