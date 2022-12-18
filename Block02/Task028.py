'''28.	Найти корни квадратного уравнения Ax² + Bx + C = 0
a.	Математикой
b.	Используя дополнительные библиотеки*'''

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

d = b**2 - 4*a*c
print('dis = ', d)

if d > 0:
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    print('x1 = ', x1, '\nx2 = ', x2)
elif d == 0:
    x = -b / 2*a
    print('x = ', x)
else:
    print('No root')

print()


import math

dis = math.sqrt(b**2 - 4*a*c)

if d > 0:
    x1 = (-b + dis)/2*a
    x2 = (-b - dis)/2*a
    print('x1 = ', x1, '\nx2 = ', x2)
elif d == 0:
    x = -b / 2*a
    print('x = ', x)
else:
    print('No root')

print()


import cmath

x1 = (-b + cmath.sqrt(d))/2*a
x2 = (-b - cmath.sqrt(d))/2*a
print('x1 =', x1, '\nx2 =', x2)