'''23.	Найти произведение пар чисел в списке. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] '''


list = []
size = int(input('Size = '))

for i in range(size):
    list.append(int(input("New number: ")))

print(list)
multiply = []
middle = int(size/2)
if size % 2 == 1:
    middle += 1

for i in range(middle):
    multiply.append(list[i]*list[-1-i])

print(multiply)
