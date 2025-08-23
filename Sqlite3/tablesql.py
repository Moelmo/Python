import sqlite3

# Koneksi ke database lokal (file .db)
conn = sqlite3.connect("belajar.db")
cursor = conn.cursor()

# Buat tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS siswa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    umur INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO siswa (nama, umur) VALUES (?, ?)", ("Budi", 16))
cursor.execute("INSERT INTO siswa (nama, umur) VALUES (?, ?)", ("Ani", 17))
conn.commit()

# Select data
cursor.execute("SELECT * FROM siswa")
for row in cursor.fetchall():
    print(row)

# Update data
cursor.execute("UPDATE siswa SET umur=? WHERE nama=?", (18, "Ani"))
conn.commit()

# Delete data
cursor.execute("DELETE FROM siswa WHERE nama=?", ("Budi",))
conn.commit()

conn.close()
