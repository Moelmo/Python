import random
import string

panjang = 12
karakter = string.ascii_letters + string.digits + string.punctuation
password_acak = ''.join(random.choices(karakter, k=panjang))

print("Password acak:", password_acak)
