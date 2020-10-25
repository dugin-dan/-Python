#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f"{self.a} + {self.b}i"

c_1 = ComplexNum(float(input("Введите действительную часть числа: ")), float(input('Введите мнимую часть числа: ')))
c_2 = ComplexNum(float(input("Введите действительную часть числа: ")), float(input('Введите мнимую часть числа: ')))
print(c_1 + c_2)
print(c_1 * c_2)