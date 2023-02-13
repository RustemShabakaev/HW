# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии. >

a = int(input("Введите число a: "))
b = int(input("Введите степень b: "))
def multiplication(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * multiplication(a, b - 1)
if a>0 and b>0:
    itog= multiplication(a,b)
    print(f'Результат возведения в степень равен: {itog}')
else:
    print("Введите другие числа")