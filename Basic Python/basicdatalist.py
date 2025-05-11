menu_item = 0
namelist = []

while menu_item != 9:
    print("----------------------------")
    print("1. Mencetak List")
    print("2. Menambahkan nama ke dalam list")
    print("3. Menghapus nama dalam list")
    print("4. mengubah data dalam list")
    print("9. keluar")
    menu_item = int(input("Pilih menu: "))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print(current, ".", namelist[current])
                current += 1
        else:
            print("list kosong")
    elif menu_item == 2:
        name = input("Masukkan nama: ")
        namelist.append(name)
    elif menu_item == 3:
        del_name = input("Masukkan nama yang ingin di hapus: ")
        if del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
        else:
            print("Nama tidak ditemukan")
    elif menu_item == 4:
        old_name = input("Masukkan nama yang ingin di ubah: ")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("Masukkan nama baru: ")
            namelist[item_number] = new_name
    else:
        print("Terimakasih sudah menggunakan progam saya")
