# Напишите программу,
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def exp(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * exp(a, b - 1)


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
print(f'{first_num} в степени {second_num} равняется {exp(first_num, second_num)}')