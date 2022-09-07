#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#для всех значений предикат.

xyz=[int(i) for i in input('Введите значения X Y Z: ').split()]


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


if checkPredicate(xyz) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")