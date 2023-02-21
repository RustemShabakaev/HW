# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

my_list = [int(i) for i in input("Введите элементы списка через пробел: ").split()]
print(my_list)
minimum = int(input('Введите миннимум: '))
maximum = int(input('Введите максимум: '))
my_list1=[]
for i in range(len(my_list)):
    if minimum <= my_list[i] and my_list[i] <= maximum:
        my_list1.append(i)
print(f'Индексы: {my_list1}')