# Задание 4

vyr = int(input("введите выручку фирмы: "))
izd = int(input("введите издержки фирмы: "))
raz = vyr - izd
ren = round((raz / vyr), 3)
if vyr > izd:
    print(f"финансовый результат - прибыль. её величина: {raz}")
    print(f"рентабельность выручки= {round(ren, 3)}")
    rab = int(input("введите численность сотрудников: "))
    raz_r = raz / rab
    print(f"прибыль фирмы в расчете на одного сотрудника = {round(raz_r, 3)}")
elif vyr == izd:
    print("финансовый результат - 0")
else:
    print(f"финансовый результат - убыток. его величина: {abs(raz)}")