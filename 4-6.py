#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
#6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
class Warehouse:
    def __init__(self, name, nums):
        self.name = name
        self.nums = nums
        self.item_dict = {self.name: self.nums}
    
    def get(self, name, nums):
        #print(self.item_dict.setdefault(self.name), type(self.item_dict.setdefault(self.name)))
        self.item_dict[self.name] = self.item_dict.get(self.name) + self.nums

class Equipment:
    def __init__(self, price, name, amount):
        self.price = price
        self.name = name
        self.amount = amount
        self.id = id

class Scanner(Equipment):
    def __init__(self, price, name, amount, type):
        super().__init__(price, name, amount)
        self.type = type

class Printer(Equipment):
    def __init__(self, price, name, amount, chromaticity):
        super().__init__(price, name, amount)
        self.chromaticity = chromaticity

class Сopier(Equipment):
    def __init__(self, price, name, amount, print_technology):
        super().__init__(price, name, amount)
        self.print_technology = print_technology

sc_1 = Scanner(250, 'HP500', 3, 'планшетный')
print(sc_1.name)
print()
d = Warehouse(sc_1.name, sc_1.amount)
print(d.get(sc_1.name, sc_1.amount))