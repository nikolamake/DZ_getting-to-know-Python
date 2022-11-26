# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            rightPart = not (x or y or z)
            leftPart = not (x) and not (y) and not (z)
            print(
                f'Значением истинности выражения X={x} Y={y} Z={z} в левой части является {rightPart} в правой {leftPart}')
