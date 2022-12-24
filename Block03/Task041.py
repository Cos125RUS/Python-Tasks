'''41.	Написать программу вычисления арифметического выражения заданного строкой.
Используются операции +,-,/,*. приоритет операций стандартный.
Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
a.	Добавить возможность использования скобок, меняющих приоритет операций.
Пример: 1+2*3 => 7; (1+2)*3 => 9;'''

def mathematic(x,y,act):
    if act == '+':
        return x+y
    elif act == '-':
        return x-y
    elif act == '*':
        return x*y
    else:#'/'
        return x/y

def priorities(nums,operation):
    print(nums)
    print(operation)

def decomposition(text):
    text += '.'
    digits = []
    nums = []
    operation = []

    for i in range(len(text)):
        if text[i].isdigit():
            digits.append(int(text[i]))
        else:
            if len(digits) > 0:
                sum = 0
                for j in range(len(digits)):
                    sum += digits[j] * 10 ** (len(digits) - 1 - j)
                nums.append(sum)
                digits = []
            operation.append(text[i])
    priorities(nums, operation)

def parentheses(text):
    arguments = text.split('(')
    for i in range(len(arguments)):
        if arguments[i].count(')') > 0:
            a = arguments[i].split(')')
            arguments[i] = a[0]
            for j in range(1, len(a)):
                arguments.insert(i+j, a[j])

    '''a = arguments[1].split(')')
    arguments[1] = a[0]
    arguments.append(a[1])'''
    print(arguments)

text = str(input('Enter: '))
if text.count('(') == 0 and text.count(')') == 0:
    decomposition(text)
else:
    parentheses(text)

