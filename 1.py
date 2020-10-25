#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    #Создаем дату
    def __init__(self, date):
        self.date = date
    @classmethod
    def transform(cls, date): # Извлекаем число, месяц, год
        day = int(date.split('-')[0])
        month = int(date.split('-')[1])
        year = int(date.split('-')[2])
        d = [day, month, year]
        return d
    @staticmethod
    def validation(d):
        month_dict_1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} # Используем решение 3 задачи 2-го урока
        month_dict_2 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} # Високосный год
        day = d[0]
        month = d[1]
        year = d[2]
        if month > 12 or month < 0:
            return "Месяц указан неверно"
        elif year < 0:
            return "Вы указываете год до нашей эры?"
        elif month in month_dict_1:
            if year % 4 == 0:
                if day > month_dict_2[month]:
                    return "День указан неверно"
                else: return "Дата указана верно"
            else:
                if day > month_dict_1[month]:
                    return "День указан неверно"
                else: return "Дата указана верно"

print(Date.transform(input("Введите дату в формате дд-мм-гггг: ")))
print(Date.validation(Date.transform(input("Введите дату в формате дд-мм-гггг: "))))