import mysql.connector

# Fungsi koneksi ke database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="belajar_python"
    )

# Tambah data siswa
def tambah_siswa():
    conn = get_connection()
    cursor = conn.cursor()

    nama = input("Masukkan nama siswa: ")
    umur = int(input("Masukkan umur siswa: "))

    sql = "INSERT INTO siswa (nama, umur) VALUES (%s, %s)"
    val = (nama, umur)
    cursor.execute(sql, val)
    conn.commit()

    print("✅ Data siswa berhasil ditambahkan!")
    conn.close()

# Lihat semua siswa
def lihat_siswa():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM siswa")
    result = cursor.fetchall()

    print("\n📋 Daftar Siswa:")
    print("----------------------------")
    for row in result:
        print(f"ID: {row[0]}, Nama: {row[1]}, Umur: {row[2]}")
    print("----------------------------\n")

    conn.close()

# Update data siswa
def update_siswa():
    conn = get_connection()
    cursor = conn.cursor()

    id_siswa = int(input("Masukkan ID siswa yang akan diupdate: "))
    nama_baru = input("Masukkan nama baru: ")
    umur_baru = int(input("Masukkan umur baru: "))

    sql = "UPDATE siswa SET nama = %s, umur = %s WHERE id = %s"
    val = (nama_baru, umur_baru, id_siswa)
    cursor.execute(sql, val)
    conn.commit()

    print("✅ Data siswa berhasil diupdate!")
    conn.close()

# Hapus data siswa
def hapus_siswa():
    conn = get_connection()
    cursor = conn.cursor()

    id_siswa = int(input("Masukkan ID siswa yang akan dihapus: "))

    sql = "DELETE FROM siswa WHERE id = %s"
    val = (id_siswa,)
    cursor.execute(sql, val)
    conn.commit()

    print("✅ Data siswa berhasil dihapus!")
    conn.close()

# Menu utama
def main():
    while True:
        print("=== MENU CRUD SISWA ===")
        print("1. Tambah Siswa")
        print("2. Lihat Semua Siswa")
        print("3. Update Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            lihat_siswa()
        elif pilihan == "3":
            update_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Keluar dari program. 👋")
            break
        else:
            print("❌ Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
