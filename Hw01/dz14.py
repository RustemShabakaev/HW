# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без
# повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint
n = int(input('Введите размер 1го множества: '))
m = int(input('Введите размер 2го множества: '))
rnd_list=[]
rnd_list1=[]
for i in range(n):
    rnd_list.append(randint(1,10))
for i in range(m):
    rnd_list1.append(randint(1,10))
print(rnd_list)
print(rnd_list1)
my_set=set(rnd_list)
my_set1=set(rnd_list1)
finalset=my_set.intersection(rnd_list1)
finalset= sorted(finalset)
print(finalset)