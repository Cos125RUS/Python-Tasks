'''37.Дан список чисел. Создать список в который попадают числа, 
описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
   [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
 Порядок элементов менять нельзя'''

list = [1, 5, 2, 3, 4, 6, 1, 7]
sequence = []

index = 0
for i in range(len(list)-1):
    for l in range(len(list) - i - 1):
        sequence.append([list[i]])
        k = 0
        for j in range(1+i+l, len(list)):
            if sequence[index][k] < list[j]:
                sequence[index].append(list[j])
                k += 1
        index += 1

max = len(sequence[0])
indexMax = 0
for i in range(len(sequence)):
    if len(sequence[i]) > max:
        max = len(sequence[i])
        indexMax = i

print(sequence[indexMax])