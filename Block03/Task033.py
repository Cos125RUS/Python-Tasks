'''33.Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
*Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

import random
file = open('C:\\repo\Python\Tasks\Block03\\file.txt', 'w')

a = random.randrange(1, 100)
b = random.randrange(0, 100)
c = random.randrange(0, 100)

k = int(2)
formula = ""
x = int

if a > 1:
    formula += (str(a) + '*')
formula += ('x^' + str(k) + ' ')
if b > 0:
    if b > 1:
        formula += ('+ ' + str(b))
    formula += '*x '
if c > 0:
    formula += ('+ ' + str(c) + ' ')
formula += '= 0'
print(formula)
file.write(formula)
file.close()