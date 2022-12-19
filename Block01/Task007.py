# 7.	Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

options = [True, False]

for i in range(2):
    for j in range(2):
        for k in range(2):
            x = options[i]
            y = options[j]
            z = options[k]
            print()
            print('x =', x, '\ty =', y, '\tz =', z, \
                '\t\t|\tnot x =', not x, '\tnot y =', not y, '\tnot z =', not z)
            print('x or y or z =', x or y or z, '  ->  not(x or y or z) =', not (x or y or z),\
                 '\t|\tnot x and not y and not z =', not x and not y and not z)
            if not (x or y or z) == (not x and not y and not z):
                print('\t\t\t\t\t\t  ',(not (x or y or z)),'=', (not x and not y and not z),\
                     '\n\t\t\t\t       not(x or y or z) = (not x and not y and not z)\
                        \n\t\t\t\t\t\t    Equality!\n')