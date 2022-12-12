# 14.	Подсчитать сумму цифр в вещественном числе.

n = float(input("n = "))
sum = 0

while n - int(n) > 0:
    n *= 10

n = int(n)
sum3 = 0
while n > 0:
    sum3 += int(n % 10)
    n = int(n/10)


print(sum3)
