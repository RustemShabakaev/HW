"""Найдите сумму цифр трехзначного числа
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)"""


number = int(input('Введите 3х значное число: '))
a = int(number % 10)
b = int(number % 100) / 10
c = int(number / 100)
i = a+c+b
print(int(i))

