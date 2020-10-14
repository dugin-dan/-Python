#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#Использовать генератор?

with open("text_5.txt", "w") as my_f:
    while True:
        num = input('Введите число или q для завершения: ')
        if num == "q":
            break
        elif num.isnumeric():
            my_f.write((num + " "))
from functools import reduce
with open("text_5.txt", "r") as my_f:
    print(reduce(lambda x,y: x + y, list(map(float,my_f.readline().split()))))
