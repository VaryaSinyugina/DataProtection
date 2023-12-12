import random


# перевод символа в 16-разрядную двоичную последовательность
def char_to_binary(character):
    binary_representation = format(ord(character), '016b')
    return binary_representation


# перевод строки из двух символов в 32-битную последовательность
def string_to_binary_sequence(input_string):
    binary_sequence = char_to_binary(input_string[0]) + char_to_binary(input_string[1])
    return binary_sequence


# получение случайной перестановки списка
def get_random_permutation(input_list):
    random.shuffle(input_list)
    return input_list


# получение списка n случайных перестановок
def get_n_random_permutations(input_list, n):
    permutations = [get_random_permutation(input_list.copy()) for _ in range(n)]
    return permutations


# шифрующий P-блок
def encrypt_p_block(binary_sequence, permutation):
    encrypted_sequence = [binary_sequence[i] for i in permutation]
    return ''.join(encrypted_sequence)


# расшифровывающий P-блок
def decrypt_p_block(binary_sequence, permutation):
    decrypted_sequence = [None] * len(permutation)
    for i, j in enumerate(permutation):
        decrypted_sequence[j] = binary_sequence[i]
    return ''.join(decrypted_sequence)


# перевод из двоичной нумерации в десятичную
def binary_to_decimal(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number


# перевод из десятичной нумерации в двоичную заданной разрядности
def decimal_to_binary(decimal_number, width):
    binary_representation = format(decimal_number, f'0{width}b')
    return binary_representation


# шифрующий S-блок
def encrypt_s_block(four_bit_sequence, permutation):
    decimal_input = binary_to_decimal(four_bit_sequence)
    encrypted_decimal_output = permutation[decimal_input]
    encrypted_four_bit_sequence = decimal_to_binary(encrypted_decimal_output, 4)
    return encrypted_four_bit_sequence


# расшифровывающий S-блок
def decrypt_s_block(four_bit_sequence, permutation):
    decimal_input = binary_to_decimal(four_bit_sequence)
    decrypted_decimal_output = permutation.index(decimal_input)
    decrypted_four_bit_sequence = decimal_to_binary(decrypted_decimal_output, 4)
    return decrypted_four_bit_sequence


# шифрование батареей S-блоков
def encrypt_s_block_battery(binary_sequence, s_block_permutations):
    split_sequences = [binary_sequence[i:i + 4] for i in range(0, len(binary_sequence), 4)]
    encrypted_sequences = [encrypt_s_block(seq, perm) for seq, perm in zip(split_sequences, s_block_permutations)]
    encrypted_sequence = ''.join(encrypted_sequences)
    return encrypted_sequence


# расшифровка батареей S-блоков
def decrypt_s_block_battery(binary_sequence, s_block_permutations):
    split_sequences = [binary_sequence[i:i + 4] for i in range(0, len(binary_sequence), 4)]
    decrypted_sequences = [decrypt_s_block(seq, perm) for seq, perm in zip(split_sequences, s_block_permutations)]
    decrypted_sequence = ''.join(decrypted_sequences)
    return decrypted_sequence


# перевод последовательности из нулей и единиц в последовательность букв
def binary_sequence_to_letters(binary_sequence):
    split_sequences = [binary_sequence[i:i + 16] for i in range(0, len(binary_sequence), 16)]
    letters = [chr(binary_to_decimal(seq)) for seq in split_sequences]
    return ''.join(letters)


def main():
    input_message = input('Введите текст: ')
    print("--- Шифрование ---")
    print("Исходное сообщение:", input_message)

    binary_form = string_to_binary_sequence(input_message)
    p_block_permutation = get_random_permutation(list(range(32)))
    encrypted_p_block = encrypt_p_block(binary_form, p_block_permutation)
    s_block_permutations = get_n_random_permutations(list(range(16)), 8)
    encrypted_s_blocks = encrypt_s_block_battery(encrypted_p_block, s_block_permutations)
    final_encrypted_sequence = encrypt_p_block(encrypted_s_blocks, p_block_permutation)
    encrypted_message = binary_sequence_to_letters(final_encrypted_sequence)

    print("Битовая форма исходного сообщения:", binary_form)
    print("Зашифрованная p-блоком битовая форма:", encrypted_p_block)
    print("Зашифрованная батареей s-блоков битовая форма:", encrypted_s_blocks)
    print("Зашифрованная p-блоком битовая форма:", final_encrypted_sequence)
    print("Зашифрованное сообщение:", encrypted_message)

    print("\n--- Расшифрование ---")

    decrypted_p_block = decrypt_p_block(final_encrypted_sequence, p_block_permutation)
    decrypted_s_blocks = decrypt_s_block_battery(decrypted_p_block, s_block_permutations)
    final_decrypted_sequence = decrypt_p_block(decrypted_s_blocks, p_block_permutation)
    decrypted_message = binary_sequence_to_letters(final_decrypted_sequence)

    print("Зашифрованное сообщение:", encrypted_message)
    print("Расшифрованное p-блоком битовая форма:", decrypted_p_block)
    print("Расшифрованная батареей s-блоков битовая форма:", decrypted_s_blocks)
    print("Расшифрованная p-блоком битовая форма:", final_decrypted_sequence)
    print("Расшифрованное сообщение:", decrypted_message)


if __name__ == "__main__":
    main()
