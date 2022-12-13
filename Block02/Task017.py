'''17.	Задать список из N элементов, заполненных числами из [-N, N]. 
Найти произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число'''

n = int(input('N = '))
list = []
sum = 0

if n > 0:
    kef = 1
else:
    kef = -1

for i in range(-n, n+kef, kef):
    list.append(i)

print(list)


pos = open('C:\\repo\Python\Tasks\Block02\\file.txt', 'r')

for num in pos:
    #print('x =', list[int(num)])
    sum += list[int(num)]

pos.close()

print('sum =', sum)
