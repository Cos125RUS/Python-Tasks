#29.Найти НОК двух чисел

a = int(input("a = "))
b = int(input("b = "))

a_denominator = {1}
b_denominator = {1}

for i in range(2, int(a/2 + 1)):
    if a % i == 0:
        a_denominator.add(i)

for i in range(1, int(b/2 + 1)):
    if b % i == 0:
        b_denominator.add(i)

nod = list(a_denominator.intersection(b_denominator)).pop()
print(nod)
print(int(a*b/nod))