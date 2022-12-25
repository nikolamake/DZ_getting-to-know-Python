#  Напишите программу вычисления арифметического выражения заданного
#  строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;


ln_in = input('Введите выражение: ')

        
def func(text, b=0, i=0):
    if text[i] == '(':
        b = i + 1
    elif text[i] == ')':
        return slice(b, i)
    return func(text, b, i + 1)
         
def aka_eval(args):
    while len(args) != 1:
        while '*' in args or '/' in args:
            try:
                prod_index = args.index('*')
            except:
                prod_index = 100
            try:
                div_index = args.index('/')
            except:
                div_index = 100

            if prod_index < div_index:
                args[prod_index -
                    1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                args.pop(prod_index + 1)
                args.pop(prod_index)
            else:
                args[div_index - 1] = int(args[div_index - 1]) / \
                    int(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)
        while '+' in args or '-' in args:
            try:
                sum_index = args.index('+')
            except:
                sum_index = 100
            try:
                deg_index = args.index('-')
            except:
                deg_index = 100

            if sum_index < deg_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + \
                    int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[deg_index - 1] = int(args[deg_index - 1]) - \
                    int(args[deg_index + 1])
                args.pop(deg_index + 1)
                args.pop(deg_index)
    print(args[0])
for k in ln_in:
    if k == '(':
        a = (ln_in[func(ln_in)])
        c= (aka_eval(a.split())) 
else:aka_eval(ln_in.split())
print(c)