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
            el = float(el)
            if not float(el):
                raise MyException("Вводите только числа!")
        except (ValueError, MyException) as err:
            print(err)
        else:
            my_list.append(float(el))