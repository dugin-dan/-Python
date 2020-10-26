def is_float(el):
    j = 0
    len(list(el))
    for i in list(el):
        if 44 <= ord(i) <= 46 or 48 <= ord(i) <= 57:
            j += 1
    if j == len(list(el)):
        return False
    else:
        return True
#print(is_float(el))

class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

flag = True
my_list = []
while flag == True:
    el = input("Введите число: ")
    if el == "q":
        flag = False
        print(my_list)
    else:
        try:
            if is_float(el):
                raise MyException("Вводите только числа!")
        except (ValueError, MyException) as err:
            print(err)
        else:
            my_list.append(float(el))