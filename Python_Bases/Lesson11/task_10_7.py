"""
7.	Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса
(комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного
результата.
"""


class ComplexNumber:
    accuracy = 17

    def __init__(self, real_part, imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.imaginary_part - self.imaginary_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part,
                             self.real_part * other.imaginary_part + self.imaginary_part * other.real_part)

    def __truediv__(self, other):
        return ComplexNumber(round((1 / (other.real_part ** 2 + other.imaginary_part ** 2)) * (
                self.real_part * other.real_part + self.imaginary_part * other.imaginary_part), ComplexNumber.accuracy),
                             round((1 / (other.real_part ** 2 + other.imaginary_part ** 2)) * (
                                     self.imaginary_part * other.real_part - self.real_part * other.imaginary_part),
                                   ComplexNumber.accuracy))

    def __str__(self):
        if self.imaginary_part > 0:
            self.imaginary_part_str = f'+{self.imaginary_part}i'
        elif self.imaginary_part < 0:
            self.imaginary_part_str = f'{self.imaginary_part}i'
        elif self.imaginary_part == 0:
            self.imaginary_part_str = ''
        return f'{self.real_part}{self.imaginary_part_str}'

    @staticmethod
    def set_accuracy(accuracy):
        ComplexNumber.accuracy = accuracy


complex_number1 = ComplexNumber(2)
complex_number2 = ComplexNumber(12, -3)
complex_number3 = ComplexNumber(2, 4)

print(complex_number3 + complex_number2)
print('-' * 200)
print(complex_number1)
print('-' * 200)
print(complex_number3 + complex_number1)
print('-' * 200)
print(complex_number3 * complex_number2)
print('-' * 200)
ComplexNumber.set_accuracy(1)
print(complex_number2 / complex_number3)
