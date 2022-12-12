#1.	По двум заданным числам проверить является ли одно квадратом второго

x = int(input('x = '))
y = int(input('y = '))

if x**2 == y:
    print("x^2 = y")
elif y**2 == x:
    print("y^2 = x")
else:
    print('No')
