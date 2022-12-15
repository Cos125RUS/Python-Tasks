# 19.Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

import time
start = int(input('start = '))
end = int(input('end = '))
list = []

for i in range(start, end):
    list.append(i)

statistics = []
difference = []
for i in range(0, end):
    statistics.append(0)
    difference.append(0)

for i in range(0, 100000000):
    milliseconds = int(round(time.time() * 1000))
    x = list[milliseconds % (end - start)]
    statistics[x] += 1
print(statistics[start:end])

mean = 0
for i in range(start, end):
    mean += statistics[i]
mean /= end-start
print("mean = ", mean)

for i in range(start, end):
    difference[i] = int(mean - statistics[i])
print(difference[start:end])