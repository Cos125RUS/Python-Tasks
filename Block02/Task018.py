# 18.	Реализовать алгоритм перемешивания списка.

import random

n = int(input('N = '))
list = []
sum = 0

for i in range(1, n+1):
    list.append(i)

print(list)

shuffle = 500
j = 0
i = 0

while j < shuffle:
    while i < n:
        index = random.randrange(0, n-1)
        change = list[i]
        list[i] = list[index]
        list[index] = change
        i+=1
    j+=1

print(list)
