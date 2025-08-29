import socket
from tqdm import tqdm  # install dulu: pip install tqdm

# Daftar port umum + service
common_ports = {
    "20": "FTP-Data",
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "67": "DHCP Server",
    "68": "DHCP Client",
    "69": "TFTP",
    "80": "HTTP",
    "110": "POP3",
    "119": "NNTP",
    "123": "NTP",
    "135": "MS RPC",
    "137": "NetBIOS Name",
    "138": "NetBIOS Datagram",
    "139": "NetBIOS Session",
    "143": "IMAP",
    "161": "SNMP",
    "179": "BGP",
    "389": "LDAP",
    "443": "HTTPS",
    "445": "SMB",
    "465": "SMTPS",
    "514": "Syslog",
    "587": "SMTP (Mail Submission)",
    "636": "LDAPS",
    "873": "rsync",
    "990": "FTPS",
    "993": "IMAPS",
    "995": "POP3S",
    "1080": "SOCKS Proxy",
    "1433": "Microsoft SQL Server",
    "1521": "Oracle Database",
    "1701": "L2TP",
    "1723": "PPTP",
    "1812": "RADIUS (Auth)",
    "1813": "RADIUS (Acct)",
    "2049": "NFS",
    "2082": "cPanel",
    "2083": "cPanel (SSL)",
    "2181": "Zookeeper",
    "2375": "Docker",
    "2376": "Docker SSL",
    "25565": "Minecraft",
    "27015": "Steam/Game Servers",
    "3306": "MySQL",
    "3389": "RDP",
    "5432": "PostgreSQL",
    "5900": "VNC",
    "5985": "WinRM HTTP",
    "5986": "WinRM HTTPS",
    "6379": "Redis",
    "8080": "HTTP-alt / Proxy",
    "8443": "HTTPS-alt",
    "9000": "SonarQube / PHP-FPM",
    "9200": "Elasticsearch",
    "11211": "Memcached",
    "27017": "MongoDB",
    "50000": "SAP"
}

target = input("Masukkan IP atau Hostname: ")

print(f"\n[+] Mulai scanning {target}...\n")

# Loop dengan tqdm untuk progress bar
for port in tqdm(range(1, 1025), desc="Scanning", unit="port"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        service = common_ports.get(port, "Tidak diketahui")
        print(f"\n[+] Port {port} TERBUKA ({service})")  # \n biar gak campur sama bar
    sock.close()

print("\nSelesai scanning!")
