# Функция шифрование текста
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha(): # Проверяем, является ли символ буквой
            is_upper = char.isupper() # Проверяем, является ли символ заглавной буквой
            char = char.lower() # Преобразуем символ в нижний регистр для работы с ним
            char_code = ord(char) - ord('a')
            char_code = (char_code + shift) % 26
            encrypted_char = chr(char_code + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Функция дешифрование текста
def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            char_code = (char_code - shift) % 26
            decrypted_char = chr(char_code + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Атака полным перебором
def caesar_bruteforce(encrypted_text):
    decrypted_variants = []
    for shift in range(26):
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        decrypted_variants.append(decrypted_text)
    return decrypted_variants


text = input("Введите текст для шифрования:")
shift = int(input("Введите число сдвига:"))

print("Оригинальный текст:", text)

encrypted_text = caesar_encrypt(text, shift)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Расшифрованный текст:", decrypted_text)

print("\nАтака полным перебором:")
decrypted_variants = caesar_bruteforce(encrypted_text)
for shift, variant in enumerate(decrypted_variants):
    print(f"Сдвиг {shift}: {variant}")
