#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))
try:
    #res = a / b
    if b == 0:
        raise MyException("На ноль делить нельзя!")
except (ZeroDivisionError, MyException) as err:
    print(err)
else:
    print(a / b)