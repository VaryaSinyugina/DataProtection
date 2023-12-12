import random

# Функция для проверки, является ли число простым
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция для нахождения НОД двух чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для генерации случайных простых чисел
def generate_prime():
    while True:
        p = random.randint(2, 100)
        if is_prime(p):
            return p

# Генерация ключей
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)# Функция Эйлера

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# Шифрование сообщения
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

# Расшифрование сообщения
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message

# Генерация ключей
public_key, private_key = generate_keys()
print("Ключи:", (public_key, private_key))

# Исходное сообщение
message = 115
print("Исходное сообщение:", message)

# Шифрование
encrypted_message = encrypt(message, public_key)
print("Зашифрованное сообщение:", encrypted_message)

# Расшифрование
decrypted_message = decrypt(encrypted_message, private_key)
print("Расшифрованное сообщение:", decrypted_message)
