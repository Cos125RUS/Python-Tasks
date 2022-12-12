# 3.	Вывести на экран числа от -N до N

n = int(input('n = '))
numbers = []

if n > 0:
    kef = 1
else:
    kef = -1

for i in range(-n, n+kef, kef):
    numbers.append(i)

print(numbers)
