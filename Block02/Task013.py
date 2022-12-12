#13.	Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def check(a,b):
    count = 0
    for i in range(len(b) - len(a) + 1):
        if a == b[i:len(a)+i]:
            count +=1
    return count

string1 = input('string1: ')
string2 = input('string2: ')

if len(string1) < len(string2):
    print(check(string1,string2))
else:
    print(check(string2,string1))