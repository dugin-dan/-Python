#4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self):
        return f"Машина повернула {self.direction}"
    def show_speed(self):
        return f"Текущая скорость {self.speed}"
    def type(self):
        return "Это полицейская машина" if self.is_police else "Это гражданское авто"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
    def show_speed(self):
        return f"Текущая скорость {self.speed} км/ч" if self.speed < 60 else "Скорость превышена"
    

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
    def show_speed(self):
        return f"Текущая скорость {self.speed}" if self.speed < 40 else "Скорость превышена"
    
class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
   
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
   
car_t = TownCar(input("Введите скорость, км/ч "), input("Введите цвет машины "), input("Введите  марку машины "), input("Это полицейская машина? (True / False) "), input("Куда поворачиваем? "))
print(f"{car_t.type()} - {car_t.color} {car_t.name}")
print(car_t.go())
print(car_t.show_speed())
print(car_t.turn())
print(car_t.stop())

car_w = WorkCar(input("Введите скорость, км/ч "), input("Введите цвет машины "), input("Введите  марку машины "), input("Это полицейская машина? (True / False) "), input("Куда поворачиваем? "))
print(f"{car_t.type()} - {car_w.color} {car_w.name}")
print(car_w.go())
print(car_w.show_speed())
print(car_w.turn())
print(car_w.stop())

car_s = SportCar(input("Введите скорость, км/ч "), input("Введите цвет машины "), input("Введите  марку машины "), input("Это полицейская машина? (True / False) "), input("Куда поворачиваем? "))
print(f"{car_t.type()} - {car_s.color} {car_s.name}")
print(car_s.go())
print(car_s.show_speed())
print(car_s.turn())
print(car_s.stop())

car_p = PoliceCar(input("Введите скорость, км/ч "), input("Введите цвет машины "), input("Введите  марку машины "), input("Это полицейская машина? (True / False) "), input("Куда поворачиваем? "))
print(f"{car_p.type()} - {car_p.color} {car_p.name}")
print(car_p.go())
print(car_p.show_speed())
print(car_p.turn())
print(car_p.stop())