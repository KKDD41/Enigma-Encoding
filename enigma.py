"""
Реализуйте функцию enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs="") с поворачивающимися и двигающимися роторами, как они описаны на предыдущем шаге.

text - исходный текст, который необходимо зашифровать
ref - номер отражателя (согласно задаче https://stepik.org/lesson/283487/step/3)
rot1, rot2, rot3 - номера роторов (согласно задаче https://stepik.org/lesson/283487/step/2)
shift1, shift2, shift3 - сдвиги роторов (1, 2 и 3, соответственно)
pairs - строка замен символов
pairs может принимать одно из 3 видов значений:

пустая строка, либо отсутствует в вызове - символы не заменяются коммутационной панелью
строка из 2 символов - только эти 2 символа заменяются ДО и ПОСЛЕ шифрования (друг на друга, см. предыдущий шаг)
строка из n пар символов, разделённых пробелом. Замены производятся в парах (друг на друга, см. предыдущий шаг) До и ПОСЛЕ шифрования
Если атрибут pairs принял недопустимое значение (например 1 символ участвует в 2 или более парах), функция enigma должна вернуть текст:

"Извините, невозможно произвести коммутацию"
"""


def create_pairs(pairs=''):
    if pairs == '':
        return dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
    else:
        pairs_list = pairs.split()
        pairs_dict = {}
        for pair in pairs_list:
            if (not pair[0].upper() in pairs_dict.keys()) and (not pair[1].upper() in pairs_dict.keys()) and len(
                    pair) == 2:
                pairs_dict[pair[0].upper()] = pair[1].upper()
                pairs_dict[pair[1].upper()] = pair[0].upper()
            else:
                return 'Извините, невозможно произвести коммутацию'
        for i in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            if not i in pairs_dict.keys():
                pairs_dict[i] = i
        return pairs_dict


def reflector(symbol, n):
    if n == 0:
        return symbol
    else:
        B_rotor = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list('YRUHQSLDPXNGOKMIEBFZCWVJAT')))
        return B_rotor[symbol]


def rotor(symbol, n, reverse=False):
    rotor = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO']
    Alphabets = []
    for i in range(3):
        Alphabets.append(dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list(rotor[i]))))
    if n == 0:
        return symbol
    if not reverse:
        return Alphabets[n - 1][symbol]
    else:
        for key in Alphabets[n - 1].keys():
            if Alphabets[n - 1][key] == symbol:
                return key


a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar(text, n):
    word = ''
    for i in text:
        if i.upper() in a:
            word += i.upper()
    Alphabet = {' ': ' '}
    for i in range(26):
        Alphabet[a[i]] = a[(i + n) % 26]
    word_0 = ''
    for i in range(len(word)):
        word_0 = word_0 + Alphabet[word[i]]
    return word_0


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=''):
    pairs_dict = create_pairs(pairs)
    if pairs_dict == 'Извините, невозможно произвести коммутацию':
        return pairs_dict
    turning_rule = {1: 17, 2: 5, 3: 22}
    res = ''
    text_to_dec_all = ''
    for i in text:
        if i.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            text_to_dec_all += i.upper()
    for text_to_dec in text_to_dec_all:
        shift3 += 1
        if turning_rule[rot3] == shift3 % 26 and turning_rule[rot2] - 1 != shift2 % 26:
            shift2 += 1
        elif turning_rule[rot2] - 1 == shift2 % 26:
            shift2 += 1
            shift1 += 1
        text_to_dec = pairs_dict[text_to_dec]
        text_to_dec = caesar(text_to_dec, shift3)
        text_to_dec = rotor(text_to_dec, rot3)
        text_to_dec = caesar(text_to_dec, 26 - shift3)
        text_to_dec = caesar(text_to_dec, shift2)
        text_to_dec = rotor(text_to_dec, rot2)
        text_to_dec = caesar(text_to_dec, 26 - shift2)
        text_to_dec = caesar(text_to_dec, shift1)
        text_to_dec = rotor(text_to_dec, rot1)
        text_to_dec = caesar(text_to_dec, 26 - shift1)
        text_to_dec = reflector(text_to_dec, ref)
        text_to_dec = caesar(text_to_dec, shift1)
        text_to_dec = rotor(text_to_dec, rot1, True)
        text_to_dec = caesar(text_to_dec, 26 - shift1)
        text_to_dec = caesar(text_to_dec, shift2)
        text_to_dec = rotor(text_to_dec, rot2, True)
        text_to_dec = caesar(text_to_dec, 26 - shift2)
        text_to_dec = caesar(text_to_dec, shift3)
        text_to_dec = rotor(text_to_dec, rot3, True)
        text_to_dec = caesar(text_to_dec, 26 - shift3)
        text_to_dec = pairs_dict[text_to_dec]
        res += text_to_dec
    return res






