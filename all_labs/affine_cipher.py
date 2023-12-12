
def mod_inverse(a, m):
    """
    Находит обратный элемент 'a' по модулю 'm'.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt(text, a, b, alphabet):
    """
    Шифрует текст 'text' с помощью аффинного шифра с ключами 'a' и 'b'.
    """
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_char_index = (a * char_index + b) % len(alphabet)
            encrypted_char = alphabet[encrypted_char_index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, a, b, alphabet):
    """
    Расшифровывает зашифрованный текст 'encrypted_text' с помощью аффинного шифра с ключами 'a' и 'b'.
    """
    decrypted_text = ""
    a_inverse = mod_inverse(a, len(alphabet))
    if a_inverse is not None:
        for char in encrypted_text:
            if char in alphabet:
                char_index = alphabet.index(char)
                decrypted_char_index = (a_inverse * (char_index - b)) % len(alphabet)
                decrypted_char = alphabet[decrypted_char_index]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
    else:
        decrypted_text = "Невозможно расшифровать. Проверьте параметр 'a'."

    return decrypted_text

if __name__ == "__main__":
    alphabet = "АОИУНТК_"  # Заданный алфавит
    original_text = "КОТИК_КАТИТ_НИТКУ"

    a = int(input("Введите значение 'a' (обратимое по модулю {}): ".format(len(alphabet))))
    b = int(input("Введите значение 'b': "))

    encrypted_text = encrypt(original_text, a, b, alphabet)
    print("Зашифрованный текст: {}".format(encrypted_text))

    decrypted_text = decrypt(encrypted_text, a, b, alphabet)
    print("Расшифрованный текст: {}".format(decrypted_text))
