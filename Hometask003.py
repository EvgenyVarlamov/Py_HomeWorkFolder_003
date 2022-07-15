# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math


def reduction(f):
    for i in range(len(f)):
        f[i] = round(f[i]-math.floor(f[i]), 2)

def difference(f):
    max_f = f[0]
    min_f = f[0]
    for i in range(len(f)):
        if max_f < f[i]:
            max_f = f[i]
        elif min_f > f[i] and f[i] != 0:
            min_f = f[i]
    return max_f-min_f

fract = [1.1, 1.2, 3.1, 5, 10.01]
reduction(fract)
print(difference(fract))