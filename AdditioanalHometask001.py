# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(arr, l):
    a, b = 1, 1
    arr[0], arr[1] = a, b
    for i in range(2, l):
        c = a+b
        arr[i] = c
        a = b
        b = c
    
def negafib(arr, l):
    a, b = 1, -1
    arr[0], arr[1] = a, b
    for i in range(2, l):
        c = a-b
        arr[i] = c
        a = b
        b = c

def output(arr, arr2):
    arr.reverse()
    arr.append(0)
    for i in range(len(arr)-1):
        arr.append(arr2[i])
    print(arr, end=' ')

n = int(input('Введите число: '))

row = ['']*n
row2 = ['']*n
negafib(row, n)
fib(row2, n)
output(row, row2)