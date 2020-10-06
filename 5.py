revenue = float(input("Введите выручку: "))
cost = float(input("Введите издержки: "))
result = revenue - cost
if result > 0:
  print("Финансовый результат - прибыль")
  print("Рентабельность - ", result / revenue)
else: print("Финансовый результат - убыток")
man = int(input("Введите численность сотрудников: "))
print("Прибыль в расчете на одного сотрудника", result / man)