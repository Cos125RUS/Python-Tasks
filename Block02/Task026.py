# 26.Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи


def fi(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fi(n-1) + fi(n-2)

def nofi(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return nofi(n+2) - nofi(n+1)

n = int(input("n = "))
numbers = []

for i in range(-n,0):
    numbers.append(nofi(i))

for i in range(0, n+1):
    numbers.append(fi(i))

print(numbers)