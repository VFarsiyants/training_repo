"""
2.	Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
— одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def textile_needed(self):
        pass


class Coat(Clothing):
    def __init__(self, size):
        self.size = size

    @property
    def textile_needed(self):
        return round(self.size / 6.5 + 0.5, 2)


class Costume(Clothing):
    def __init__(self, height):
        self.height = height

    @property
    def textile_needed(self):
        return round(2 * self.height + 0.3, 2)


my_coat = Coat(48)
my_costume = Costume(180)

print(my_coat.textile_needed)
print(my_costume.textile_needed)
print(f'Для одного пальто и одного костюма нужно {my_coat.textile_needed + my_costume.textile_needed} ткани')
