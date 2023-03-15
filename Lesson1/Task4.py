# Задание 4

vyr = int(input("Введите выручку фирмы: "))
izd = int(input("Введите издержки фирмы: "))
raz = vyr - izd
ren = round((raz / vyr), 3)
if vyr > izd:
    print(f"Финансовый результат - прибыль. Ее величина: {raz}")
    print(f"Рентабельность выручки= {round(ren, 3)}")
    rab = int(input("Введите численность сотрудников: "))
    raz_r = raz / rab
    print(f"Прибыль фирмы в расчете на одного сотрудника = {round(raz_r, 3)}")
elif vyr == izd:
    print("Финансовый результат - 0")
else:
    print(f"Финансовый результат - убыток. Его величина: {abs(raz)}")