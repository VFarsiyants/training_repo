"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

string1 = 'aabab'
string2 = 'acdfgh'
string3 = 'wqacacwqac'


def substrings_counter(base_string):
    """
    :param base_string: string where should be each possible substring quantity calculated
    :return: dictionary with substring as key and quantity in string as value
    """
    result = {}
    base_string_len = len(base_string)
    # go by each possible substring length
    for i in range(1, base_string_len):
        # go by each possible substring of this length
        for j in range(base_string_len - i + 1):
            # index of substring after end in base string
            k = j + i
            subs = base_string[j:k]
            # if we already calculated entities for this substring, go to next substring
            if subs in result.keys():
                continue
            # there is no sense to look in entire string, only in tale
            tale = base_string[k:]
            has_subs = hashlib.sha1(bytes(subs.encode('utf-8'))).hexdigest()
            # substring in this string occurs at least 1 time
            count_sub = 1
            for x in range(len(tale) - i + 1):
                if hashlib.sha1(bytes(tale[x:x + i].encode('utf-8'))).hexdigest() == has_subs:
                    count_sub += 1
            result[subs] = count_sub
    return result


result1 = substrings_counter(string1)
result2 = substrings_counter(string2)
result3 = substrings_counter(string3)

for k, v in result3.items():
    print(f'{k}: {v}')
