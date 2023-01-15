#42.Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#a.входные и выходные данные хранятся в отдельных текстовых файлах

with open('Source.txt','r') as file:
    file = file.read() + ' '

with open('RLE.txt', 'w') as rle:
    while len(file) > 1:
        i = 1
        while file[0] == file[i]:
            i += 1
        rle.write(f'{ord(file[0])} {i}\n')
        file = file[i:]


with open('RLE.txt','r') as file:
    rle = dict(map(lambda f: f.split(), (line.replace('\n','') for line in file)))
with open('Unpacked.txt', 'w') as file:
    for i in rle.keys():
        file.write(chr(int(i)) * int(rle[i]))
