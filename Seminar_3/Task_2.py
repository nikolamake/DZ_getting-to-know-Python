# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
#     *Пример:*
#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
lst = [1.1, 1.2, 3.1, 5.1, 10.01]
lst_mod = []
max = lst[0] % 1
min = lst[1] % 1
if (max >= min):
    for i in range(2, len(lst)):
        if (lst[i] % 1 > max):
            max = lst[i] % 1
        elif (lst[i] % 1 < min):
            min = lst[i] % 1
else:
    max = min
    min = max
    for i in range(0, len(lst)):
            if (lst[i] % 1 > max):
                max = lst[i] % 1
            elif (lst[i] % 1 < min):
                min = lst[i] % 1
difference = round((max - min),3)
print(f'Разницу между максимальным и минимальным значением дробной части элементов списка равна: {difference}')
