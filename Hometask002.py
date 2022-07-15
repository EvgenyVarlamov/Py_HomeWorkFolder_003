# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

def pair_multiple(list):
    s = '[ '
    for i in range(int(math.ceil(len(list)/2))):
        s += f'{list[i]*list[-(i+1)]} '
    s += ']'
    return s

pair = [2, 3, 4, 5, 6]
print(pair_multiple(pair))