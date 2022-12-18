#25.Написать программу преобразования десятичного числа в двоичное

n = int(input("N = "))

list = []

while n > 1:
    list.append(n%2)
    n = int(n/2)

list.append(n)

newList = []

for i in range(int(len(list)/2)):
    x = list[i]
    list[i] = list[-1 - i]
    list[-1 -i] = x

if len(list) > 0:
    res = 1

for i in range(1,len(list)):
    res *= 10
    res += list[i]

print(res)
