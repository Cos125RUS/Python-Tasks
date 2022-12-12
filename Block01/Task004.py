#4.	Показать первую цифру дробной части числа

n = float(input('n = '))
z = int(n)
ost = n - z
if ost == 0:
    print("Дробной части нет")
else:
    ost *= 10
    z = int(ost)
    print(z)