#Вычислить число π c заданной точностью d
#Пример: при d = 0.001,π = 3.141.10^(-1)≤d≤10^(-10)

p = str(3.141592653589793)
print('10^(-1)≤d≤10^(-10)')
'''d = float(input('d = '))
count = 2
while d < 1:
    d *= 10
    count += 1

pi = float(p[0:count])
print(f'π = {pi}')'''

d = input('d = ')
print(f'π = {p[:len(d)]}')

#Подумать, что если точность вычисления до 1000 знаков после запятой
d = int(input('Сколько вешать в знаках?   '))
print('π = 3.', end = '')
with open('C:\\repo\Python\Tasks\Block02\pi.txt', 'r') as pi:
    print(pi.read(d))