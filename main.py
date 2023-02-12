# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
print(f'Сумма {first_num} и {second_num} равняется {sum(first_num, second_num)}')