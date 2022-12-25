# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.

# код первоначальной программы
# import random
# import collections
# quantity = int(input('Введите количество элементов списка: '))
# min_value = int(input('Введите минимальное значение в списке: '))
# max_value = int(input('Введите максимальное значение в списке: '))
# rand_list=[] 
# for i in range(quantity):
#     rand_list.append(random.randint(min_value,max_value))
# b = collections.Counter(rand_list)
# unique_list = [i[0]  for i  in b.items() if i[1] == 1]
# print(f'Исходный список : {rand_list}')
# print(f'Список неповторяющихся элементов исходной последовательности:{unique_list}')

# изменённый код программы
import random
quantity = int(input('Введите количество элементов списка: '))
min_value = int(input('Введите минимальное значение в списке: '))
max_value = int(input('Введите максимальное значение в списке: '))
rand_list=[] 
for i in range(quantity):
    rand_list.append(random.randint(min_value,max_value))
unique_list = list(filter(lambda a: rand_list.count(a) == 1, rand_list))
print(f'Исходный список : {rand_list}')
print(f'Список неповторяющихся элементов исходной последовательности:{unique_list}')
