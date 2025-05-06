# gampang nya

# if begini:
#     maka ini 
# else begini:
#     maka itu
# elif:
#     pokoknya gitu dah

# progam penghitung tingkat berdasarkan nilai

N = int(input("Masukkan Nilai :"))
if N >= 90:
    G = "A+"
elif N >= 85:
    G = "B+"
elif N >= 80:
    G = "C+"
elif N >= 75:
    G = "A"
elif N >= 70:
    G = "B"
elif N >= 65:
    G = "C"
elif N >= 60:
    G = "D"
elif N >= 55:
    G = "E"
else:
    G = "F"

print(f"Nilai mu {N} anda mendapat grade {G}")