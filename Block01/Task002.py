#2.	Найти максимальное из пяти чисел


numbers = []
i = 0

while i < 5:
    num = int(input('number%d = ' % (i+1)))
    numbers.append(num)
    i += 1
print(numbers)

max = numbers[0]

for i in numbers:
    if i > max:
        max = i

print('max = ', max)
