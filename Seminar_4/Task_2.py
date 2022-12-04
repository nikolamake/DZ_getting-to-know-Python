# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N. 
# (Выполнили на семинаре)


num = int(input('Введите натуральное число: '))
multipliers = []
div = 2
while num > 1:
    while num % div == 0:
        multipliers.append(div)
        num //= div
    div += 1
print(f'Список простых множителей числа : {multipliers}')
