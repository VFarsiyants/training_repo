"""
1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = dd_mm_yyyy

    @classmethod
    def info_extraction(cls, dd_mm_yyyy):
        dd = int(dd_mm_yyyy[:2])
        mm = int(dd_mm_yyyy[3:5])
        yyyy = int(dd_mm_yyyy[-4:])
        return dd, mm, yyyy

    @staticmethod
    def number_validation(dd, mm, yyyy):
        if dd > 31 or dd < 1:
            print('Проверка не пройдена, день должен быть в промежутке между 1 и 31')
        if mm > 12 or mm < 1:
            print('Проверка не пройдена, месяц должен быть в промежутке между 1 и 12')
        if yyyy < 1:
            print('Проверка не пройдена, год меньше 1 не поддерживается')


Date.number_validation(31, 1, 1999)
print('-----------------------------------')
Date.number_validation(31, 13, 2021)
print('-----------------------------------')
Date.number_validation(32, 11, 0)
print('-----------------------------------')
print(Date.info_extraction('21-05-2021'))
print(Date.info_extraction('21-05-2021')[0])
print(Date.info_extraction('21-05-2021')[1])
print(Date.info_extraction('21-05-2021')[2])
