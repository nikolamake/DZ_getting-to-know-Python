# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]
lst_mod = []
if (len(lst) % 2 != 0):
    for i in range(0, len(lst) // 2 + 1):
        lst_mod.append(lst[i] * (lst[len(lst) - i - 1]))
else:
    for i in range(0, len(lst) // 2):
        lst_mod.append(lst[i] * (lst[len(lst) - i - 1]))
print(lst_mod)
