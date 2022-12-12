#11.	Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('N = '))
list = [1]

for i in range(0,n-1):
    list.append(list[i] * -3)

print(list)