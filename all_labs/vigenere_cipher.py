# Функция шифрования текста
def vigenere_encrypt(text, keyword):
    encrypted_text = ""
    keyword = keyword.lower()  # Преобразуем ключевое слово в нижний регистр для удобства
    keyword_len = len(keyword)
    for i, char in enumerate(text):
        if char.isalpha():  # Проверяем, является ли символ буквой
            is_upper = char.isupper()  # Проверяем, является ли символ заглавной буквой
            char = char.lower()  # Преобразуем символ в нижний регистр для работы с ним
            keyword_char = keyword[i % keyword_len]  # Получаем текущий символ ключевого слова
            shift = ord(keyword_char) - ord('a')  # Вычисляем сдвиг на основе символа ключевого слова
            char_code = ord(char) - ord('a')  # Получаем числовое представление символа текста
            char_code = (char_code + shift) % 26  # Применяем сдвиг к символу
            encrypted_char = chr(char_code + ord('a'))  # Преобразуем числовой код обратно в символ
            if is_upper:  # Если исходный символ был заглавной буквой, делаем зашифрованный символ тоже заглавной
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char  # Добавляем зашифрованный символ к строке
        else:
            encrypted_text += char  # Если символ не является буквой, оставляем его без изменений
    return encrypted_text

# Функция дешифрования текста
def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = ""
    keyword = keyword.lower() # Преобразуем ключевое слово в нижний регистр для удобства
    keyword_len = len(keyword)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            is_upper = char.isupper() # Проверяем, является ли символ заглавной буквой
            char = char.lower()
            keyword_char = keyword[i % keyword_len]
            shift = ord(keyword_char) - ord('a')
            char_code = ord(char) - ord('a')
            char_code = (char_code - shift) % 26
            decrypted_char = chr(char_code + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text



text = input("Введите текст для шифрования:")
keyword = input("Введите ключевое слово:")

print("Оригинальный текст:", text)

encrypted_text = vigenere_encrypt(text, keyword)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, keyword)
print("Расшифрованный текст:", decrypted_text)
