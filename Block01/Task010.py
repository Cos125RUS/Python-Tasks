#10.	Найти расстояние между двумя точками пространства

from math import sqrt


dotA = []
dotB = []

i = 0

while i < 2:
    x = int(input(f'A{i+1} = '))
    y = int(input(f'B{i+1} = '))
    dotA.append(x)
    dotB.append(y)
    i +=1

distance = sqrt((dotB[0] - dotA[0])**2 + (dotB[1] - dotA[1])**2)
print('Distance = %4.2f' %distance)