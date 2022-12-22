#35.В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.

with open('C:\\repo\Python\Tasks\Block03\list_of_nums.txt','r') as file:
    nums = file.readlines()

nums = nums[0].split()
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums) - 1):
    if nums[i] != nums[i+1] - 1:
        find = nums[i] + 1
        
print(find)