"""
3.	Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться
"""


class NumListValidationError(Exception):
    def __init__(self, item):
        super().__init__(f'Введено не число {item}')


num_list1 = []

while True:
    prompt = input('>')
    if prompt == 'stop':
        break
    else:
        try:
            if not prompt.lstrip('-').isdigit():
                raise NumListValidationError(prompt)
        except NumListValidationError:
            print('Введено не число')
        else:
            num_list1.append(prompt)
            print(f'Число добавлено в чписок. Список чисел в списке: {" ".join(num_list1)}')