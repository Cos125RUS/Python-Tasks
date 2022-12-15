# 20.Определить, присутствует ли в заданном списке строк, некоторое число

def check(a, b):
    count = 0
    for i in range(len(b) - len(a) + 1):
        if a == b[i:len(a)+i]:
            count += 1
    return count


listOfStrings = []
for i in range(5):
    listOfStrings.append(input("New string: "))

n = int(input("n = "))
num = str(n)
sum = 0

for i in range(5):
    x = check(num, listOfStrings[i])
    print(f'In line {i} the number {n} occurs {x} times')
    sum += x

print()
print(f"In all lines: {sum}")