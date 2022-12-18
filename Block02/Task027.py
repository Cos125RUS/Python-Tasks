#27.Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел

string = "321 56 894 46 61 431"

nums = string.split(' ')
print(nums)

max = int(nums[0])
min = int(nums[0])

for i in range(1, len(nums)):
    if int(nums[i]) > max:
        max = int(nums[i])
    if int(nums[i]) < min:
        min = int(nums[i])

print('max = ', max)
print('min = ', min)