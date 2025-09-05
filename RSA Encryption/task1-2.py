import random
import math
import sympy

def random_nbit_prime(n):
    return sympy.randprime(2**(n-1), 2**n)

def gcd(a, b):
    """İki sayının en büyük ortak bölenini (EBOB) bulur."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y

def modinv(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modüler ters bulunamadı')
    else:
        return x % phi

bits = [2,4,8,16,32]
selected_prime_tuples = []
for i in bits:
  x = random_nbit_prime(i)
  y = random_nbit_prime(i)
  while (y==x):
    y = random_nbit_prime(i)
  selected_prime_tuples.append((x,y))
print(selected_prime_tuples)

def generate_keys(p, q):
    """RSA public ve private key'leri üretir."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Public key (e) genellikle 65537 olarak seçilir
    e = 3
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Private key (d) hesaplanır
    d = modinv(e, phi)

    return (e, n), (d, n)


key_pairs = []
for p, q in selected_prime_tuples:
    public_key, private_key = generate_keys(p, q)
    key_pairs.append((public_key, private_key))

print("\nGenerated Key Pairs:")
for i, (public_key, private_key) in enumerate(key_pairs):
    print(f"Key Pair {i+1}:")
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    print()


def encrypt_int(plaintext_int, public_key):
    e, n = public_key
    ciphertext_int = pow(plaintext_int, e, n)  # Şifreleme: c = m^e mod n
    return ciphertext_int

def decrypt_int(ciphertext_int, private_key):
    d, n = private_key
    plaintext_int = pow(ciphertext_int, d, n)  # Şifre çözme: m = c^d mod n
    return plaintext_int

def generate_int_message_for_n(n):
    """n değerinden küçük rastgele bir tamsayı mesajı oluşturur."""
    max_message_value = n - 1  # n'den küçük olmalı
    message_int = random.randint(0, max_message_value)
    return message_int

plaintext_list=[]
ciphertext_list=[]
print("Encryption and Decryption:")
for i, (public_key, private_key) in enumerate(key_pairs):
    print(f"Key Pair {i+1}:")
    e, n = public_key  # n değerini public_key'den al
    message_int = generate_int_message_for_n(n)  # n'ye göre dinamik mesaj oluştur
    print(f"Generated Integer Message: {message_int}")

    # Şifreleme
    ciphertext = encrypt_int(message_int, public_key)

    plaintext_list.append(message_int)
    ciphertext_list.append(ciphertext)

    print(f"Ciphertext: {ciphertext}")
    # Şifre çözme
    decrypted_message = decrypt_int(ciphertext, private_key)
    print(f"Decrypted Message: {decrypted_message}")
    print()

import time

def brute_force_factorization(n):
    """Attempts to factorize n by checking divisibility from 2 to sqrt(n)."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i  # Return the factors p and q
    return None, None  # If no factors found

def brute_force_rsa_attack(public_key, ciphertext):
    """Attempts to break RSA encryption by brute force factorization."""
    e, n = public_key

    start_time = time.time()
    p, q = brute_force_factorization(n)
    end_time = time.time()

    elapsed_time = end_time - start_time

    if p is None or q is None:
        print("Factorization failed.")
        return None, None, None, elapsed_time

    print(f"Factors found: p={p}, q={q} (Time taken: {elapsed_time:.4f} seconds)")

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute private key d
    d = modinv(e, phi)

    # Decrypt the ciphertext
    decrypted_message = decrypt_int(ciphertext, (d, n))
    return decrypted_message, p, q, d, elapsed_time


import matplotlib.pyplot as plt

print("\nBrute Force Attack:")
time_taken = []
bit_sizes = []

for i, (public_key, private_key) in enumerate(key_pairs):
    bit_size = public_key[1].bit_length()
    print(f"Attempting to break Key Pair {i+1} (Bit size: {bit_size})...")
    decrypted_message, p, q, d, elapsed_time = brute_force_rsa_attack(public_key, ciphertext_list[i])

    if decrypted_message is not None:
        print(f"Successfully decrypted message: {decrypted_message}")
        print(f"Private Key d: {d}\n")
    else:
        print("Brute-force attack failed.\n")

    time_taken.append(elapsed_time)
    bit_sizes.append(bit_size)

# Plot the results
plt.figure(figsize=(8,5))
plt.plot(bit_sizes, time_taken, marker='o', linestyle='-', color='b')
plt.xlabel("Bit Size of n")
plt.ylabel("Time Taken (seconds)")
plt.title("Brute Force Factorization Time vs Bit Size")
plt.grid(True)
plt.show()