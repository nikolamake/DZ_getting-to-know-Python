# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# код первоначальной программы

# lst = []
# num = int(input('Введите число: '))
# composition = 1
# for i in range(1, num + 1):
#     composition = i * composition
#     lst.append(str(composition))
# print("[" + ", ".join(lst) +"]")

# изменённый код программы

from math import factorial
num = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,num+1)))))