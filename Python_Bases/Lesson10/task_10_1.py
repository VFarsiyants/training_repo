"""
1.	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86

3	5	32
2	4	6
-1	64	-8

3	5	8	3
8	3	7	1


Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, numbers):
        if not isinstance(numbers, list):
            raise ValueError('Необходимо передать список списков с числами')
        string_length = len(numbers[0])
        # определяю кол-во символов в поле элемента матрицы, для красивого отображения
        self.__field_length = 2
        self.numbers = []
        for item in numbers:
            if not isinstance(item, list) and string_length != len(item):
                raise ValueError('различное число элементов в строках матрицы')
            for number in item:
                if not isinstance(number, int or float):
                    raise ValueError('элементами матрицы должны быть числа')
                # если есть число с большим кол-вом знаков, величина поля под элемент изменится
                if len(str(number)) >= self.__field_length:
                    self.__field_length = len(str(number)) + 1
            self.numbers.append(item)

    def __str__(self):
        return '\n'.join(
            [('\t'.join([f'{item:>{self.__field_length}}' for item in string])) for string in self.numbers])

    def __add__(self, other):
        if len(self.numbers) != len(other.numbers) or len(self.numbers[0]) != len(other.numbers[0]):
            raise ValueError('Складываемые матрицы имеют различную структуру')
        return Matrix([[self.numbers[i][j] + other.numbers[i][j] for j in range(len(self.numbers[0]))] for i in
                       range(len(self.numbers))])


obj1 = Matrix([[31, 22], [37, 43], [51, 86]])
obj2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
obj3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
obj4 = Matrix([[0, 12, -9], [8, 43, 16], [-21, 37, 15]])
print(obj1)
print('-------------------------------')
print(obj2)
print('-------------------------------')
print(obj3)
print('-------------------------------')
print(obj4)
print('-------------------------------')
obj5 = obj2 + obj4
print(obj5)
# obj6 = obj2 + obj1
# print(obj6)
# Вызовет исключение, так как складываем матрицы различной размерности
