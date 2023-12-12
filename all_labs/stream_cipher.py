import random

def print_long_list(_msg, _l: list):
    print(_msg, end=': ')
    print('[', end='')
    for _ in _l:
        print(_, end=', ')
    print(']')

def get_key(_gen: list, _l: list) -> list:
    _p = _l[:]
    len_list = len(_l)
    seed = 2 * len_list
    for n in range(seed):
        i = random.randint(0, len_list - 1)
        j = random.randint(0, len_list - 1)
        if (i != j) and (_p[i] != _p[j]):
            _p[i], _p[j] = _p[j], _p[i]
    print_long_list("Ключ", _p)

    gen = _p
    _gen_temp = gen
    _j = 0
    for _i in range(256):
        _j = (_j + _gen_temp[_i] + _p[_i]) % 256
        _gen_temp[_i], _gen_temp[_j] = _gen_temp[_j], _gen_temp[_i]
    return _gen_temp


def char_to_bits(_c: str, _positions: int) -> str:
    return bin(ord(_c))[2:].zfill(_positions)

def num_to_bitstr(_num: int, _positions: int) -> str:
    return bin(_num)[2:].zfill(_positions)

def from_bits_to_number(_s: str) -> int:
    _string = _s[::-1]
    _num = 0
    for _i in range(len(_string)):
        _num += int(_string[_i]) * (2 ** _i)
    return _num

def from_unicode_to_ascii(_s: str) -> list:
    _lst = []
    for _elem in _s:
        _lst.append(char_to_bits(_elem, 16)[:8])
        _lst.append(char_to_bits(_elem, 16)[8:])
    return [from_bits_to_number(_elem) for _elem in _lst]

def make_gamma(_gen: list, _message: list) -> list:
    _gamma = []
    _gen_temp = _gen[:]
    _i, _j = 0, 0
    for _k in range(len(_message)):
        _i = (_i + 1) % 256
        _j = (_j + _gen_temp[_i]) % 256
        _gen_temp[_i], _gen_temp[_j] = _gen_temp[_j], _gen_temp[_i]
        _t = (_gen_temp[_i] + _gen_temp[_j]) % 256
        _gamma.append(_gen_temp[_t])
    return _gamma

def chifering(_message: list, _gamma: list) -> list:
    return [(_message[_i] ^ _gamma[_i]) for _i in range(len(_message))]

def symbolise(_l: list) -> str:
    _s = ""
    _i = 0
    while _i < len(_l):
        _s += chr(from_bits_to_number(num_to_bitstr(_l[_i], 8) + num_to_bitstr(_l[_i + 1], 8)))
        _i += 2
    return _s

gen = [None for x in range(256)]
gen = get_key(gen, list(range(256)))
print_long_list("Инициализированный генератор случайных чисел", gen)

print("Введите вариант сообщения:")
print("1 - пример готового сообщения для шифрования")
print("2 - написать свое сообщение")
num_var = input("Выбор: ")

def choice(num_var):
    if num_var == '1':
        msg = "Hello, world!"
        return msg
    elif num_var == '2':
        msg = input("Введите сообщение: ")
        return msg
    else:
        print("Введено неверное число.")


message = choice(num_var)
print("Сообщение: ", message)


print_long_list("Коды юникода символов сообщения", [ord(letter) for letter in message])

splitted_message = from_unicode_to_ascii(message)
print_long_list("Пары байтов сообщения", splitted_message)

gamma = make_gamma(gen, splitted_message)
print_long_list("Гамма", gamma)

chifred_message = chifering(splitted_message, gamma)
print_long_list("Зашифрованное сообщение (список)", chifred_message)

symbolised_message = symbolise(chifred_message)
print("Шифрованное сообщение (символы юникода): " + symbolised_message)

desplitted_message = from_unicode_to_ascii(symbolised_message)
dechifred_message = chifering(desplitted_message, gamma)
print_long_list("Расшифрованное сообщение (список)", dechifred_message)
print("Расшифрованное сообщение (символы юникода): " + symbolise(dechifred_message))