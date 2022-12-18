'''17.	Задать список из N элементов, заполненных числами из [-N, N]. 
Найти произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число'''

import random

n = int(input('N = '))
list = []
sum = 0

for i in range(n):
    list.append(random.randrange(-n, n+1))

print(list)

pos = open('C:\\repo\Python\Tasks\Block02\\file.txt', 'r')

for num in pos:
    #print('x =', list[int(num)])
    sum += list[int(num)]

pos.close()

print('sum =', sum)
