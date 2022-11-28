# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

lst = []
num = int(input('Введите число: '))
composition = 1
for i in range(1, num + 1):
    composition = i * composition
    lst.append(str(composition))
print("[" + ", ".join(lst) +"]")