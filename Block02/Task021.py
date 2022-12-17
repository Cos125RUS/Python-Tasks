'''21.	Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1'''


def findString(list, string):
    count = 0
    answer = -1

    for i in range(len(list)):
        if string == list[i]:
            count += 1
            if count == 2:
                answer = i

    print(f'Answer is {answer}')


list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
string1 = "qwe"

list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
string2 = "йцу"

list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
string3 = "йцу"

list4 = ["123", "234", 123, "567"]
string4 = "123"

list5 = []
string5 = "123"

allLists = [list1, list2, list3, list4, list5]
allStrings = [string1, string2, string3, string4, string5]

for i in range(len(allLists)):
    findString(allLists[i], allStrings[i])
