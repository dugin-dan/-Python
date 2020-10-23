#3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *\n*\n*..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *\n*\n.
#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: ***\n*\n*.
#Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
        return self.n - other.n if self.n - other.n > 0 \
        else f"{self.n} < {other.n} - вычитание невозможно"
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return round(self.n / other.n)
    def make_order(self, el):
        return '\n'.join(['*' * el for _ in range(self.n // el)]) + '\n' + '*' * (self.n % el)

c_1 = Cell(int(input("введите число клеток ")))
c_2 = Cell(int(input("введите число клеток ")))
r = int(input("введите число клеток в ряду "))
c_s = c_1 + c_2
print(c_1 + c_2)
print(Cell(c_1 + c_2).make_order(r))
print(c_1 - c_2)
print(Cell(c_1 - c_2).make_order(r))
print(c_1 * c_2)
print(Cell(c_1 * c_2).make_order(r))
print(c_1 / c_2)
print(Cell(c_1 / c_2).make_order(r))