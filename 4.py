#4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
#Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]
#from sys import argv
#n, m = argv
n = int(input('Введите нижнюю границу: '))
m = int(input('Введите верхнюю границу списка: '))
#from random import randint
import random
#my_list = [random.randint(n,m) for i in range(2 * (m - n))]
#print([random.randint(n,m) for i in range(2 * (m - n))])
print([el for el in [random.randint(n,m) for i in range(2 * (m - n))] if [random.randint(n,m) for i in range(2 * (m - n))].count(el) == 1])