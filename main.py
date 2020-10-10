#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 2 3 4 = 24.
#from sys import argv
#n, m = argv
n = int(input('Введите нижнюю границу: '))
m = int(input('Введите верхнюю границу списка: '))
#from random import randint
import random
#my_list = [random.randint(n,m) for i in range(2 * (m - n))]
#print([random.randint(n,m) for i in range(2 * (m - n))])
print([el for el in [random.randint(n,m) for i in range(2 * (m - n))] if [random.randint(n,m) for i in range(2 * (m - n))].count(el) == 1])