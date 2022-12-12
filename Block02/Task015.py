#15.	Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]


n = int(input('N = '))
list = []

for i in range(1,n+1):
    res = 1
    for j in range(1,i+1):
        res *= j
    list.append(res)

print(list)