# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: 
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите длину ряда: '))
f1 = f2 = 1
lst_positiv = [1, 1]
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    lst_positiv.append(f2)

lst_negativ = []
for i in range(0, len(lst_positiv)):
    if(i % 2 != 0):
        lst_negativ.append(lst_positiv[i] * - 1)
    else:
        lst_negativ.append(lst_positiv[i])
lst_negativ.reverse()
lst_negativ.append(0)
lst_Fib = []
lst_Fib = lst_negativ + lst_positiv
print(lst_Fib)