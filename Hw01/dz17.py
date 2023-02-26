# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows
# и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация
# строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

x=int(input('Введите x= '))
y=int(input('Введите y= '))
operation=(lambda x, y: x * y)
def printOperationTable(operation, x, y):
    for i in range(1,x+1):
        print('\n')
        for j in range(1,y+1):
            calc=(operation(i,j))
            print(f'{calc:>4}', end=' ')

printOperationTable(operation,x,y)