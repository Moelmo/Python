import mysql.connector

# koneksi data bese ke sekolah

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "sekolah"
)

try:
    cursor = conn.cursor()
    print(f"Berhasil memuat databese")
except:
    print(f"Gagal memuat databese")

print("\n" * 10)

def tambah_siswa(nis, nama, kelas):
    sql = "INSERT INTO siswa (nis, nama, kelas) VALUES (%s, %s, %s)"
    values = (nis, nama, kelas)
    cursor.execute(sql, values)
    conn.commit()
    print(f"Data siswa berhasil di tambahkan")

def lihat_siswa():
    cursor.execute("SELECT * FROM siswa")
    result = cursor.fetchall()
    print("\n=====[ Data Siswa ]=====")
    if not result:
        print("Tidak ada data siswa")
    for row in result:
        print(f"ID  :   {row[0]}    |   NiS : {row[1]}  |   Nama    :   {row[2]}    |   Kelas   :   {row[3]}")
    while True:
        enter = input("Tekan enter untuk lanjut")
        if enter == "":
            main()
            break
        else:
            main()
            break

def hapus_siswa(nis):
    try:
        int_nis = int(nis)
    except ValueError:
        while True:
            print("Nis harus berupa angka")
            enter = input("Tekan enter untuk lanjut")
            if enter == "":
                main()
                break
            else:
                main()
                break

    cursor.execute("SELECT nis, nama, kelas FROM siswa WHERE nis = %s", (int_nis,))
    row = cursor.fetchone()
    if row:
        print("Data yang ditemukan")
        print(f"Nis     :   {row[0]}")
        print(f"Nama    :   {row[1]}")
        print(f"Kelas   :   {row[2]}")
        confirm = input("Anda yakin untuk menghapus data ini? (y/n) >> ").lower()
        if confirm == "y":
            cursor.execute("DELETE FROM siswa WHERE nis = %s", (int_nis,))
            print(f"Data {row[1]} Berhasil di hapus")
            conn.commit()
    else:
        print("Data tidak ditemukan")
    
    while True:
        enter = input("Tekan enter untuk lanjut")
        if enter == "":
            main()
            break
        else:
            main()
            break

def main():
    print("\n" * 10)
    print("Selamat datang di data sekolah")
    print("1. Tambah siswa")
    print("2. Lihat Data")
    print("3. Hapus Data siswa")
    print("4. Keluar")
    select = input("Select >> ")
    if select == "1":
        print("isi data berikut")
        while True:
            try:
                nis = int(input("Masukkan NIS       : "))
                break
            except ValueError:
                print("Masukkan nis dengan angka bukan huruf")
            
        while True:
            nama = input("Masukkan nama murid       : ")
            if len(nama) < 3:
                print("Nama terlalu pendek! Maksimal 3 karakter.")
                continue
            
            if len(nama) > 50:
                print("Nama terllau panjang! Maksimal 50 karakter.")
                continue
            break

        while True:
            kelas = input("Masukkan kelas murid     : ")
            if len(kelas) < 3:
                print("Nama terlalu pendek! Maksimal 3 karakter.")
                continue
            
            if len(kelas) > 20:
                print("Nama terllau panjang! Maksimal 20 karakter.")
                continue
            break

        try:
            tambah_siswa(nis, nama, kelas)
            print("=======[Data Sussces]=======")
            print(f"Nis     : {nis}")
            print(f"Nama    : {nama}")
            print(f"Kelas   : {kelas}")
            print("==[Data berhasil disimpan]==")
            main()
        except ValueError:
            print("Data gagal tersimpan")

    elif select == '2':
        lihat_siswa()

    elif select == "3":
        nis = input("Masukkan nis siswa yang ingin anda hapus >> ")
        hapus_siswa(nis)

    elif select == "4":
        print("Terimakasih sudah menggunakan program kami")

    else:
        print("Masukkan angka (1/2)")
        main()


main()
