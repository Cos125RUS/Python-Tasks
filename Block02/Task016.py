# Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

n = int(input('n = '))
list = []
sum = 0

for i in range(1, n+1):
    list.append((1+1/i)**i)
    sum += list[i-1]

print(list)
print('%.2f' %sum)