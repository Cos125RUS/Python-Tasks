#38.Напишите программу, удаляющую из текста все слова содержащие "абв"

text = "вапабввап апрапр ватвабвиваи ропрьтабвпр ваываыв апрапр"
newText = ""
text = text.split()

for i in range(len(text)):
    if not text[i].count("абв"):
        newText += (text[i] + ' ')

print(newText)