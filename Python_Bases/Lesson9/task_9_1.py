import time
import datetime


class TrafficLight:
    __color = 'red'

    def running(self, max_time_of_work):
        """
        Что бы скрипт не работал вечность, передаем методу максимальное время работы светофора
        :param max_time_of_work: максимальное время работы светофора по истечению которого свтофор остановит свою
        работу после включения зеленого света
        :return: None
        """
        now = datetime.datetime.now()
        interval = 0
        while interval < max_time_of_work:
            print(self.__color)
            if self.__color == 'red':
                time.sleep(7)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                time.sleep(2)
                self.__color = 'green'
            else:
                time.sleep(15)
                print('\n______________________________\n')
                self.__color = 'red'
                interval = (datetime.datetime.now() - now).total_seconds()


tl = TrafficLight()
tl.running(60)
