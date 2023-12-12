import random

class Hemming:
    def __init__(self, message, alphabet):
        self.rnd = random.Random(4)
        self.alp = alphabet
        self.str = message
        self.m = int((len(alphabet) + 1).bit_length())
        self.k = 1
        while self.k + self.m + 1 > 2 ** self.k:
            self.k += 1
        self.n = 2 ** self.k - 1
        self.mat = None
        self.seqs = self.get_list()

    def get_list(self):
        res_list = []
        for i in range(len(self.str)):
            ind = self.alp.index(self.str[i])
            res = list(f"{ind:0{self.m}b}")
            self.mat = [[0] * (self.k + self.m) for _ in range(self.k)]
            for j in range(self.k):
                width = 2 ** j
                pos = width - 1
                while pos < self.k + self.m:
                    for w in range(width):
                        if pos + w >= self.k + self.m:
                            break
                        self.mat[j][pos + w] = 1
                    pos += width * 2
            for j in range(self.k):
                res.insert(2 ** j - 1, '?')
            for j in range(self.k):
                s = sum(int(res[b]) for b in range(2 ** j, self.k + self.m) if self.mat[j][b] == 1)
                res[2 ** j - 1] = '0' if s % 2 == 0 else '1'
            res_list.append(res)
        return res_list

    def check_and_fix(self):
        ok = True
        for i in range(len(self.seqs)):
            source = ''.join(map(str, self.seqs[i]))
            cmp = list(self.trim_control_bits(self.seqs[i]))
            for j in range(self.k):
                cmp.insert(2 ** j - 1, '?')
            for j in range(self.k):
                s = sum(int(cmp[b]) for b in range(2 ** j, self.k + self.m) if self.mat[j][b] == 1)
                cmp[2 ** j - 1] = '0' if s % 2 == 0 else '1'
            for j in range(self.k):
                s = sum(int(cmp[b]) for b in range(2 ** j, self.k + self.m) if self.mat[j][b] == 1)
                pos = 2 ** j
                if s % 2 != int(source[pos - 1]):
                    ok = False
                    ind = -1
                    for b in range(self.k):
                        step = 2 ** b
                        if cmp[step - 1] != source[step - 1]:
                            ind += step
                    self.seqs[i][ind] = '0' if self.seqs[i][ind] == '1' else '1'
                    print(f"ERROR в последовательности #{i + 1}, в ячейке {ind + 1}")
                    break
        return ok

    def decode(self):
        res = ''
        for s in self.seqs:
            ind = int(self.trim_control_bits(s), 2)
            res += self.alp[ind]
        return res

    def corrupt_message(self):
        for s in self.seqs:
            self.corrupt_one_cell(s)

    def corrupt_one_cell(self, s):
        ind = self.rnd.randint(0, len(s) - 1)
        s[ind] = '0' if s[ind] == '1' else '1'

    def trim_control_bits(self, s):
        res = ''.join(map(str, s))
        for i in range(self.k - 1, -1, -1):
            res = res[:2 ** i - 1] + res[2 ** i:]
        return res


def main():
    alp_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    #alp_en = "abcdefghijklmnopqrstuvwxyz"
    message = "привет"
    print("\nНачальное сообщение: ", message)

    print("\nШифрование")
    hemm = Hemming(message, alp_ru)
    for s in hemm.seqs:
        print(''.join(map(str, s)))

    print("\nИскажение")
    hemm.corrupt_message()
    for s in hemm.seqs:
        print(''.join(map(str, s)))

    print("\nПоиск ошибки и расшифровка")
    hemm.check_and_fix()
    print("\nРасшифрованное сообщение:", hemm.decode())


if __name__ == "__main__":
    main()
