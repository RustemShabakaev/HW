# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


a = int(input('Введите 3х значное число: '))
b = int(a % 10)
c = int(a % 100) / 10
d = int(a / 100)
i = b+c+d
print(int(i))

