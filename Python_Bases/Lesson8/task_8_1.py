'''
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
">>> email_parse('someone@geekbrains.ru')"
{'username': 'someone', 'domain': 'geekbrains.ru'}
">>> email_parse('someone@geekbrainsru')"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru


Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
данном случае использовать функцию re.compile()?
'''

import re


def email_parse(email_address):
    email_address = email_address.lower()
    if not re.match(r'[a-z][^а-яё]+[@][a-z]+\.[a-z]+', email_address):
        raise ValueError(f'wrong email: {email_address}')
    email_data = {}
    email_raw_data = re.split(r'@', email_address)
    email_data['username'] = email_raw_data[0]
    email_data['domain'] = email_raw_data[1]
    return email_data


if __name__ == "__main__":
    print(email_parse('Farsiyanc@icloud.com'))
    # print(email_parse('farsiyanc@icloud-com'))
    # print(email_parse('farкаiyanc@icloud-com'))
    # print(email_parse('_farsiyanc@icloud-com'))
    # print(email_parse('farsiyancicloud-com'))
