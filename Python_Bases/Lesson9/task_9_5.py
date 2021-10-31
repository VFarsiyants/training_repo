class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Ведение записи ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Штриховка карандашом')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Выделение маркером')


blue_pen = Pen('Синяя ручка')
gray_pencil = Pencil('Простой серый карандаш')
rad_handle = Handle('Желтый маркер')

blue_pen.draw()
gray_pencil.draw()
rad_handle.draw()
