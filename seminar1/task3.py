#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
#и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

xy=[int(i) for i in input('Введите X Y: ').split()]
if xy[0] == 0 and xy[1] == 0:
    print("Неверное значение")
def checkCoordinates(xy):
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    elif xy[0] > 0 and xy[1] < 0:
        text = 4
    print(f"Точка находится в {text} четверти плоскости")



checkCoordinates(xy)