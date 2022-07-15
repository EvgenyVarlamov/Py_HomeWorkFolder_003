# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число: '))
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(int(b))

def bin_func(n):
    bin = ''
    while n > 0:
        bin = str(n % 2) + bin
        n = n//2
    return bin

dec = int(input('Введите число: '))
print(bin_func(dec))