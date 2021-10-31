"""
2.	Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class OwnZeroDivision(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class DivisionMachine:
    def __init__(self, number_to_divide, divider):
        self.number_to_divide = number_to_divide
        self.divider = divider

    @property
    def division_result(self):
        if self.divider == 0:
            raise OwnZeroDivision(f'делитель не может быть равным 0')
        else:
            return self.number_to_divide / self.divider


try:
    a = float(input('Введите делимое число '))
    b = float(input('Введите делитель '))
    dividing = DivisionMachine(12, 0)
    result = dividing.division_result
except OwnZeroDivision:
    print('Делитель не может быть меньше 0')
except ValueError:
    print('Введено не число')
else:
    print(f'Результат деления {result}')
