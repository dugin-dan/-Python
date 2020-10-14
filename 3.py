#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open("text_3.txt", "r") as my_f:
    my_dict = {float(line.split(" ")[1]): line.split(" ")[0] for line in my_f}
print(my_dict)
#for i in my_dict.keys():
    #if i < 20000: print(my_dict.get(i))
print([my_dict.get(i) for i in my_dict.keys() if i < 20000])
sum = 0
for i in my_dict.keys():
    sum += i
print(sum / len(my_dict.keys()))