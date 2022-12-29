'''41.	Написать программу вычисления арифметического выражения заданного строкой.
Используются операции +,-,/,*. приоритет операций стандартный.
Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
a.	Добавить возможность использования скобок, меняющих приоритет операций.
Пример: 1+2*3 => 7; (1+2)*3 => 9;'''


'''def mathematic(text):
    print(text)
    text += '.'
    nums = []
    operation = []
    s = 0
    for i in range(len(text)):
        if not text[i].isdigit():
            nums.append(text[s:i])
            s = i+1
            operation.append(text[i])
    print(nums)
    print(operation)
    res = ""
    for i in range(len(operation)-1):
        if operation[i] == '*' or operation[i] == '/':
            a = str(int(nums[i])*int(nums[i+1]) if operation[i] == '*' else int(nums[i])/int(nums[i+1]))
            nums[i + 1] = a
            res += a
    for i in range(len(operation)-1):
        if operation[i] == '+' or operation[i] == '-':
            a = str(int(nums[i])+int(nums[i+1]) if operation[i] == '+' else int(nums[i])-int(nums[i+1]))
            nums[i + 1] = a
            res += a
    return res'''

def action(n1,n2,operation):
    if operation == '*' or operation == '/':
        return str(n1 * n2 if operation == '*' else n1 / n2)
    else:
        return str(n1+n2 if operation == '+' else n1-n2)

def mathematic(text, count, op1, op2):
    for n in range(count):
        for i in range(len(text)):
            if text[i] == op1 or text[i] == op2:
                operation = i
                num1 = i-1
                while text[num1].isdigit() and num1 > 0:
                    num1 -= 1
                if num1 > 0:
                    num1 += 1
                num2 = i+1
                while num2+1 < len(text) and text[num2+1].isdigit():
                    num2 += 1
                res = str(action(int(text[num1:operation]), int(text[operation+1:num2+1]), text[operation]))
                text = text.replace(text[num1:num2+1], res, 1)
                break
    return text
def priority(text):
    count = text.count('*') + text.count('/')
    if count > 0:
        text = mathematic(text, count, '*', '/')
    count = text.count('+') + text.count('-')
    if count > 0:
        text = mathematic(text, count, '+', '-')
    return text

def parentheses(text):
    count = text.count('(')
    if count > 0:
        for n in range(count):
            for i in range(len(text)):
                if text[i] == '(':
                    start = i + 1
            for i in range(start, len(text)):
                if text[i] == ')':
                    end = i
                    text = text.replace(text[start-1:end+1], priority(text[start:end]))
                    break
    text = priority(text)
    return text

text = str(input('Enter: '))
text = parentheses(text)
print(f'Result = {text}')
