# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

ascii_start = 32
ascii_end = 127
string = ""

for i in range(ascii_start, ascii_end + 1):
    string += f'code {i:<3} - "{chr(i)}"\t'
    if (i + 1 - ascii_start) % 10 == 0:
        print(string)
        string = ''
else:
    print(string)
