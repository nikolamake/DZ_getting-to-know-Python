# Доделать задание в группах: Создать калькулятор для работы 
# с рациональными и комплексными числами, 
# организовать меню, добавив в неё систему логирования.


# блок кода позволит пользователю выбрать: продолжить работу 
# с программой или завершить её
import sys
from fractions import Fraction
import logging 



def calculator_main(): #для выбора типа чисел
    operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    1 для работы с целыми и десятичными числами
    2 для работы с рациональными числами
    3 для работы с комлексными числами
    
    ''')
    if operation == '1':
        calculator_decimal()
    elif operation == '2':
        calculato_fraction()
    elif operation == '2':
        calculato_fraction()
    elif operation == '3':
        calculator_comprehensiven()
    else: 
        print('Номер отсутствует, пожалуйста, введите операцию из списка!')
        calculator_main()

def again():
    calc_again = input(''' 
Вы хотите посчитать ещё раз?
Пожалуйста, введите Y для ответа "ДА" или N для ответа "НЕТ".
    ''')
    if calc_again.upper() == 'Y': #  upper позволяет вводить без учета к регистру
        calculator_main()
    elif calc_again.upper() == 'N':
        print('До новых встреч')
        sys.exit(0) #для выхода из системы
    else:
        again()

def calculator_decimal(): #для десятичных и целых чисел
    operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    + для сложения
    - для вычитания
    * для умножения
    / для деления
    ''')
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        print('Вы ввели неверную операцию, пожалуйста, введите операцию из списка!')
        calculator_decimal()
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))
    if operation == '+':
        print('{} + {} = {}'.format(number_1, number_2,number_1 + number_2))
    elif operation == '-':
        print('{} - {} = {}'.format(number_1, number_2,number_1 - number_2))
    elif operation == '*':
        print('{} * {} = {}'.format(number_1, number_2,number_1 * number_2))
    else:
        print('{} / {} = {}'.format(number_1, number_2,number_1 / number_2))
    again()

def calculato_fraction(): #для работы с рациональными числами
    operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    + для сложения
    - для вычитания
    * для умножения
    / для деления
    ''')
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        print('Вы ввели неверную операцию, пожалуйста, введите операцию из списка!')
        calculato_fraction()
    numerator_1 = int(input("Введите числитель первой  дроби: "))
    denominator_1 = int(input("Введите знаменатель первой дроби: "))
    numerator_2 = int(input("Введите числитель второй дроби: "))
    denominator_2 = int(input("Введите знаменатель второй дроби: "))
    if operation == '+':
        print(Fraction(numerator_1,denominator_1) + Fraction(numerator_2,denominator_2))
    elif operation == '-':
       print(Fraction(numerator_1,denominator_1) - Fraction(numerator_2,denominator_2))
    elif operation == '*':
        print(Fraction(numerator_1,denominator_1) * Fraction(numerator_2,denominator_2))
    else:
        print(Fraction(numerator_1,denominator_1) / Fraction(numerator_2,denominator_2))
    again()
def calculator_comprehensiven(): #для работы с рациональными числами
    operation = input('''
    Пожалуйста, введите математическую операцию, которую вы хотели бы выполнить:
    + для сложения
    - для вычитания
    * для умножения
    / для деления
    ''')
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        print('Вы ввели неверную операцию, пожалуйста, введите операцию из списка!')
        calculator_comprehensiven()
    valid_1 = int(input("Введите действительную часть первого числа: "))
    imaginary_1 = int(input("Введите мнимую часть первого числа: "))
    valid_2 = int(input("Введите действительную часть второго числа: "))
    imaginary_2 = int(input("Введите мнимую часть первого числа: "))
    if operation == '+':
        print(complex(valid_1,imaginary_1) + complex(valid_2,imaginary_2))
    elif operation == '-':
       print(complex(valid_1,imaginary_1) - complex(valid_2,imaginary_2))
    elif operation == '*':
        print(complex(valid_1,imaginary_1) * complex(valid_2,imaginary_2))
    else:
       print(complex(valid_1,imaginary_1) / complex(valid_2,imaginary_2))
    again()



#Create and configure logger using the basicConfig() function 
logging.basicConfig(filename="newfile.csv", 
               format='%(asctime)s %(message)s', 
               filemode='a') 
 
#Creating an object of the logging 
logger=logging.getLogger('calculator_main')


 
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 
 
#Test messages 
# logger.debug("This is a harmless debug Message") 
logger.info(f'{calculator_main}') 
# logger.warning("It is a Warning. Please make changes") 
# logger.error("You are trying to divide by zero") 
# logger.critical("Internet is down")  
 
calculator_main()



