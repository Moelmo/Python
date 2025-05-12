# aplikasi topup versi terminal untuk membuat logic sebelum ke web



def main():
    print("############################################")
    print("Hallo Selamat Datang Di Aplikasi Top-Up Kami")
    print("############################################\n")
    print("List Produk Kami Yang Tersedia")
    print("1. Pulsa")
    print("2. Paket Data")
    print("3. E-Wallet")
    print("4. Tranfer Bank")
    print("5. Game")
    print("9. Keluar")
    print("############################################\n")

    produk = 0 

    while produk != 9:
        produk = input("Pilih produk anda yang ingin di beli : ")
        if produk == "1":
            print("Pulsa")
        else:
            print("Masukkan input yang benar")

main()