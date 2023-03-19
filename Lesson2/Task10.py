n = int(input('Введите количество монет: '))
count_o = count_r = 0
for i in range(n):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        count_o += 1
    else:
        count_r += 1
if count_o > count_r:
    print(f'Переверните {count_r} монет с решки на орла, их меньше всего')
elif count_o == count_r:
    print(f'Количество орлов и решек одинаково, по {count_o} шт.')
else:
    print(f'Переверните {count_o} монет с орла на решку, их меньше всего')