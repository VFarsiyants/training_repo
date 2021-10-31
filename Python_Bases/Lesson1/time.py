"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
* до часа: <m> мин <s> сек;
* до суток: <h> час <m> мин <s> сек;
* *до месяца, до года, больше года: по аналогии.
"""


def print_time(ss):
    seconds = str(ss % 60) + " ceк "
    minutes = str(int(ss / 60) % 60) + " мин " if int(ss / 60) % 60 else ""
    hours = str(int(ss / (60 * 60)) % 24) + " час " if int(ss / (60 * 60)) % 24 else ""
    days = str(int(ss / (60 * 60 * 24) % 30.4167)) + " дн " if int(ss / (60 * 60 * 24)) % 30.4167 else ""
    month = str(int(ss / (60 * 60 * 24 * 30.4167)) % 12) + " мес " if int(ss / (60 * 60 * 24 * 30.4167) % 12) else ""
    years = str(int(ss / (60 * 60 * 24 * 30.4167 * 12))) + " лет " if int(ss / (60 * 60 * 24 * 30.4167 * 12)) else ""
    return print(years + month + days + hours + minutes + seconds)


if __name__ == '__main__':
    duration = int(input('Введите длительность в секундах: '))
    print_time(duration)
