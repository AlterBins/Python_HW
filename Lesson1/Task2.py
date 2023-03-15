# Задание 2

count_sec = int(input("Введите время в секундах: "))
min_sec = count_sec / 60
hour_sec = count_sec / 3600
print(f"Время в формате ч:м:с - {round(hour_sec, 2)}:{round(min_sec, 2)}:"
      f"{count_sec}")
