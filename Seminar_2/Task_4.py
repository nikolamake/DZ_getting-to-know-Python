# Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

lst = []
num = int(input('Введите число: '))
for i in range(-num, num + 1):
    lst.append(str(i))
print(f'Массив элементов от -{num} до {num}')
print("[" + ", ".join(lst) + "]")

lst1 = []
data = open('file.txt', 'r')
for line in data:
    lst1.append(str(line))
    print(int(line), end=' ' )
data.close()

composition = 1
for k in range(0, len(lst1)):
    composition = composition * int(lst[int(lst1[k])])
print(f'Произведение элементов из массива на позициях из file.txt: {composition}')