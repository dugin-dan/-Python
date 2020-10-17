#3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
    
    def income(self):
        return self._income.get("wage") + self._income.get("bonus")

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        

    def get_full_name(self):        
        print(f"Сотрудник {self.name}  {self.surname} занимает должность {self.position}")
    
    def get_total_income(self):
        print(f"Полный доход составляет {Worker.income(self)}")

m_1 = Position(input("Введите имя: "), input("Введите фамилию: "), input("Введите должность: "), float(input("Введите оклад: ")), float(input("Введите премию: ")))
m_1.get_full_name()
m_1.get_total_income()