#34.Даны два файла в каждом из которых находится запись многочлена. 
#Сформировать файл содержащий сумму многочленов.

def odds(enter):
    formula = enter.replace(' ', '')
    if formula.count('x^2') > 0:
        f = formula.split(sep = 'x^2')
        if len(f[0]) > 0:
            a = int(f[0][0:len(f[0]) - 1])
        else: a = 1
        
        if f[1].count('+') > 0:
            f = f[1].split(sep = '+', maxsplit = 1)
    else: 
        a = 0
        f = ["",formula]

    if f[1].count('x') > 0:
        f = f[1].split(sep = 'x')
        if len(f[0]) > 0:
            b = int(f[0][0:len(f[0]) - 1])
        else: b = 1

        if f[1].count('+') > 0:
            f = f[1].split(sep = '+', maxsplit = 1)
    else: b = 0

    f = f[1].split(sep = '=')
    if len(f[0]) > 0:
        c = int(f[0][0:len(f[0]) - 1])
    else: c = 0

    k = [a,b,c]
    return k

with open('C:\\repo\Python\Tasks\Block03\\f1.txt', 'r') as formula1:
    f1 = formula1.readlines()
with open('C:\\repo\Python\Tasks\Block03\\f2.txt', 'r') as formula2:
    f2 = formula2.readlines()

formula1 = ""
formula1 += f1[0]
formula2 = ""
formula2 += f2[0]

k1 = odds(formula1)
k2 = odds(formula2)
k = [k1[0]+k2[0], k1[1]+k2[1],k1[2]+k2[2]]
formula = ""

if k[0] > 1:
    formula += (str(k[0]) + '*')
formula += ('x^' + str(2) + ' ')
if k[1] > 0:
    if k[1] > 1:
        formula += ('+ ' + str(k[1]))
    formula += '*x '
if k[2] > 0:
    formula += ('+ ' + str(k[2]) + ' ')
formula += '= 0'
print(formula)

with open('C:\\repo\Python\Tasks\Block03\\f_res.txt','w') as res:
    res.write(formula)
