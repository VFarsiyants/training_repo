"""
4.	Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5.	Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за приём оргтехники на склад и
передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class Engine:
    def __init__(self):
        print('Начало работы')
        print('-' * 200)
        while True:
            print('Введите команду')
            print('-' * 200)
            print(
                'Принять на склад\nПолучить информацию об остатках\nПолучить детальную информацию об остатках\n'
                'Выдать технику\n''Получить информацию о выданной технике''\nЗавершить работу')
            command = input('>').lower()
            print('-' * 200)
            if command == 'принять на склад':
                Warehouse.item_acceptance()
            elif command == 'получить информацию об остатках':
                Warehouse.get_stocks_info()
            elif command == 'получить детальную информацию об остатках':
                Warehouse.get_stocks_detailed_info()
            elif command == 'выдать технику':
                Warehouse.give_item()
            elif command == 'получить информацию о выданной технике':
                Warehouse.get_department_items()
            elif command == 'завершить работу':
                print('Программа завершена')
                break
            else:
                print(
                    'Список доступных комманд:\nПринять на склад\nПолучить информацию об остатках\nВыдать технику\n',
                    'Получить информацию о выданной технике\nЗавершить работу')
                print('-' * 200)


class Warehouse:
    device_types = ['Принтер', 'Сканнер', 'Ксерокс']
    items = []
    given_items = {}

    def __init__(self):

        self.qty_on_warehouse = 0

    @classmethod
    def item_acceptance(cls):
        print(f'Введите тип устройства (доступные типы устройств {", ".join(Warehouse.device_types)})')
        item_type = input('>')
        try:
            if item_type not in Warehouse.device_types:
                raise ValueError('Введен неизвестный тип устройства')
        except ValueError:
            print(f'Операция отменена, доступные типы устройств: {", ".join(Warehouse.device_types)}')
        else:
            if item_type == 'Принтер':
                Warehouse.items.append(Printer())
            elif item_type == 'Ксерокс':
                Warehouse.items.append(Xerox())
            elif item_type == 'Сканер':
                Warehouse.items.append(Scanner())
            print('Устройство принято на склад')
            print('-' * 200)

    @classmethod
    def get_stocks_detailed_info(cls):
        if Warehouse.items:
            print('Техника на складе')
            for item in Warehouse.items:
                print(item)
                print('_' * 200)
        else:
            print('Склад пустой')
            print('_' * 200)

    @classmethod
    def get_stocks_info(cls):
        if Warehouse.items:
            result_types = []
            result_qtys = []
            for item in Warehouse.items:
                if item.device_type not in result_types:
                    result_types.append(item.device_type)
                    result_qtys.append(1)
                else:
                    result_qtys[result_types.index(item.device_type)] += 1
            for item_type, qty in zip(result_types, result_qtys):
                print(f'Тип оборудования: {item_type}. Кол-во на складе: {qty}')
                print('_' * 200)
        else:
            print('Склад пустой')
            print('_' * 200)

    @classmethod
    def give_item(cls):
        if not Warehouse.given_items:
            print('Техника не выдавалась')
        else:
            try:
                print('Введите тип необходимого устройства')
                item_type = input('>')
                if item_type not in Warehouse.device_types:
                    raise ValueError
            except ValueError('Незивестный тип техники'):
                print(f'Операция отменена доступные типы устройств: {", ".join(Warehouse.device_types)}')
            else:
                print(f'Введите название отдела ({", ".join(Warehouse.given_items.keys())})')
                department = input('>')
                try:
                    if item_type not in Warehouse.device_types:
                        raise ValueError('Введен неизвестный тип устройства')
                except ValueError:
                    print(f'Операция отменена, доступные типы устройств: {", ".join(Warehouse.device_types)}')
                else:
                    given_item = None
                    for item in Warehouse.items:
                        if item.device_type == item_type:
                            Warehouse.items.remove(item)
                            given_item = item
                            if department in Warehouse.given_items.keys():
                                Warehouse.given_items[department].append(item)
                                print('Устройство выдано')
                                print('_' * 200)
                            else:
                                Warehouse.given_items[department] = [item]
                                print('Устройство выдано')
                                print('_' * 200)
                            break
                    if not given_item:
                        print('На складе нет доступной техники данного типа')
                        print('_' * 200)

    @classmethod
    def get_department_items(cls):
        print('Введите название отдела')
        department = input('>')
        if department not in Warehouse.given_items.keys():
            print('Отдел не запрашивал оргтехнику')
            print('_' * 200)
        else:
            print('Техника числящаяся за отделом')
            for item in Warehouse.given_items[department]:
                print(item)
                print('-' * 200)


class OfficeEquip:
    count = 0

    def __init__(self):
        OfficeEquip.count += 1
        print('Введите имя устройства')
        self.name = input('>')
        print('Введите название модели')
        self.model = input('>')
        print('Укажите год выпуска')
        try:
            self.year = input('>')
            if not self.year.isdigit() or (int(self.year) < 1950) or (int(self.year) > 2021):
                raise ValueError('Введено недопустимое значение года выпуска')
        except ValueError:
            print('Недопустимое значение. Введите заново данные устройства')
            self.__init__()

    def __str__(self):
        return f'Имя устройства {self.name}, Модель {self.model}, Год выпуска {self.year}'


class Printer(OfficeEquip):
    def __init__(self):
        super().__init__()
        self.device_type = 'Принтер'
        print('Принтер цветной? ')
        self.is_color = True if input('>') == ('Да' or 'да') else False
        print('Поддерживается печать с двух сторон ')
        self.is_multi_side = True if input('>') == ('Да' or 'да') else False

    def __str__(self):
        return super().__str__() + f'\nПоддержка цветной печати: \t{"да" if self.is_color else "нет"}\n' \
                                   f'Поддержка двусторонней печати: \t{"да" if self.is_multi_side else "нет"}'


class Xerox(OfficeEquip):
    def __init__(self):
        self.device_type = 'Ксерокс'
        super().__init__()
        print('Укажите поставщика ксерокса')
        self.producer = input('>')

    def __str__(self):
        return super().__str__() + f'\nПоставщик ксерокса: \t{self.producer}'


class Scanner(OfficeEquip):
    def __init__(self):
        self.device_type = 'Сканнер'
        super().__init__()
        print('Возможность сканирования нескольких страниц')
        self.is_multi_page = input('>')

    def __str__(self):
        return super().__str__() + f'\nПоставщик ксерокса: \t{"да" if self.is_multi_page else "нет"}'


start = Engine()
