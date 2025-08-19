import ipaddress

def subnet_calculator(ip_cidr):
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)

        print(f"IP Address      : {ip_cidr.split('/')[0]}")
        print(f"Netmask         : {network.netmask}")
        print(f"Network Address : {network.network_address}")
        print(f"Broadcast Addr  : {network.broadcast_address}")
        print(f"Jumlah Host     : {network.num_addresses - 2} (usable)")
        print(f"IP Range        : {list(network.hosts())[0]} - {list(network.hosts())[-1]}")

    except ValueError as e:
        print("Input tidak valid. Gunakan format IP/CIDR (contoh: 192.168.1.1/24)")

# Contoh penggunaan:
ip_input = input("Masukkan IP dan CIDR (misal 192.168.1.10/24): ")
subnet_calculator(ip_input)
