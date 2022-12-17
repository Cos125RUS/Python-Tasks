#22.Найти сумму чисел списка стоящих на нечетной позиции

list = []
size = 10

for i in range(size):
    list.append(int(input("New number: ")))

print(list)
sum = 0

for i in range(1,size,2):
    sum += list[i]

print('sum = ',sum)