# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0.56 -> 11

num = float(input('Введите число: '))
if (num < 0):
    num = - num
wholePart = int(num // 1)
fractionalPart = int(str(num).split('.')[1])
sum_wholePart = 0  # сумма цифр целой части части
i = 1
while ((wholePart // i) > 0):
    sum_wholePart = int(sum_wholePart + (wholePart // i) % 10)
    i *= 10
sum_fractionalPart = 0  # сумма цифр дробной части
k = 1
while ((fractionalPart // k) > 0):
    sum_fractionalPart = int(sum_fractionalPart + (fractionalPart // k) % 10)
    k *= 10
sumNumbers = sum_wholePart + sum_fractionalPart
if (num >= 0):
    print(f'Сумма цифр модуля числа {num} : {sumNumbers}')
