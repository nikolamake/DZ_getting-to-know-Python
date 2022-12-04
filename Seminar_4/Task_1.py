# Вычислить число ПИ c заданной точностью d
#     *Пример:* 
#     - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10
import math
d = str(input('Введите точность числа π: '))
num1 = str(d).split('.')[1]
count = 0
for i in range(len(num1)):
    count+=1
print(f'Число π c точностью {d} равняется: {str(math.pi)[:count + 2]}')





