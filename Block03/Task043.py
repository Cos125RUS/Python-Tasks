'''43.Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]'''

nums = [1, 2, 3, 5, 1, 5, 3, 10]
unique = []
for i in nums:
    if nums.count(i) == 1:
        unique.append(i)

print(unique)