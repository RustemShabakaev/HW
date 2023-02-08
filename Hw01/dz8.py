# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint
x = int(input('Введите искомое число Х: '))
n = int(input('Введите размер сравниваемого списка: '))
rnd_list=[]
countX= 0
minRaznoct=100
for i in range(0, n, 1):
    rnd_list.append(randint(1, 100))
print(rnd_list)
for i in range(0, n, 1):
    if rnd_list[i]==x:
        countX+=1
    else:
        if x>rnd_list[i]:
           y= x-rnd_list[i]
           if y<minRaznoct:
               minRaznoct=y
               nearElement=rnd_list[i]
        else:
           y= rnd_list[i] - x
           if y < minRaznoct:
            minRaznoct = y
            nearElement=rnd_list[i]
if countX!=0:
    print(f'Искомое число встречается : {countX}')
else:
    print(f'Ближайшее число : {nearElement}')
