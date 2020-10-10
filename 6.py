#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
#Объединить а) и б). Не использовать break

from sys import argv

st_num, st, f_num, rep = argv
#st_num = int(input('Введите начальное значение: '))
#st = int(input('Введите шаг: '))
#f_num = int(input('Введите конечное значение: '))
#rep = int(input('Введите кратность повторов элементов: '))

from itertools import count
from itertools import cycle
nums = []
for el in count(st_num,st):
    if el > f_num:
        break
    else:
        nums.append(el)
print(nums)

rep_nums = []
i = 1
for el in cycle(nums):
    if i <= len(nums):
        for c in range(rep): rep_nums.append(el)
        i += 1
    else: break
print(rep_nums)