class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        print('auto is running')
        self.speed = speed

    def stop(self):
        print('auto is stopped')
        self.speed = 0

    def turn(self, direction):
        print(f'auto is turning on {direction}')

    def show_speed(self):
        print(f'speed {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'speed {self.speed}. It\'s speeding!')
        else:
            print(f'speed {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'speed {self.speed}. It\'s speeding!')
        else:
            print(f'speed {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


city_taxi = TownCar(50, 'yellow', 'taxi', False)
city_fancy_car = SportCar(90, 'red', 'ferrari', False)
city_trash_collector = WorkCar(30, 'gray', 'garbage truck', False)
city_police_car = PoliceCar(90, 'black', 'FBI detective', True)

city_taxi.show_speed()
city_taxi.go(70)
city_taxi.show_speed()
city_taxi.turn('left')
city_taxi.stop()
city_taxi.show_speed()
print('________________________')
city_fancy_car.show_speed()
city_fancy_car.go(110)
city_fancy_car.show_speed()
city_fancy_car.turn('right')
city_fancy_car.stop()
city_fancy_car.show_speed()
print('________________________')
city_trash_collector.show_speed()
city_trash_collector.go(50)
city_trash_collector.show_speed()
city_trash_collector.turn('right')
city_trash_collector.stop()
city_trash_collector.show_speed()
print('________________________')
city_police_car.show_speed()
city_police_car.go(130)
city_police_car.show_speed()
city_police_car.turn('left')
city_police_car.stop()
city_police_car.show_speed()
