# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

number = int(input('Введите целое число:'))
numberFib1 = 1
numberFib2 = 1
summa = 0
i = 3
while summa < number:
    summa = numberFib1 + numberFib2
    i += 1
    if summa == number:
        print(f'число с индексом {i} = {summa}')
    elif summa > number: print('-1')
    numberFib1 = numberFib2
    numberFib2 = summa
