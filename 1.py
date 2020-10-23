#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
#Формируем матрицу. Число строк и столбцов задается пользователем при создании объекта
    def init(self):
        self.tab = []
        self.columns = int(input("Введите число столбцов: "))
        self.rows = int(input("Введите число строк: "))
        for j in range(self.rows):
            self.row = []
            for i in range(self.columns):
                self.el = float(input("Введите следующий элемент таблицы: "))
                self.row.append(self.el)
                self.tab.append(self.row)

    def __str__(self):
            return '\n'.join(['\t'.join([str(i) for i in j]) for j in self.tab]) 

    def __add__(self, other):
        self.new_tab = []
        for j in range(self.rows):
            self.r = []
            for i in range(self.columns):
                self.r.append(self.tab[j][i] + other.tab[j][i])
                self.new_tab.append(self.r)
                for self._ in self.new_tab:
                    print(self._)   
m_1 = Matrix()
m_2 = Matrix()

print(m_1)
print()
print(m_2)
print()
print(m_1 + m_2)