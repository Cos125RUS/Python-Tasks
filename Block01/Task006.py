#6.	Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

d = int(input('Enter the day '))
if 0 > d or d > 7:
    print("В неделе всего 7 дней, чувак")
elif d > 5:
    print("Выходной")
else:
    print("Унылые серые будни")