#Напишите программу, которая принимает на вход координаты двух точек
#и находит расстояние между ними в 2D пространстве.

print('Введите координаты точки А:')
xA = float(input('X: '))
yA = float(input('Y: '))
print("Введите координаты точки B:")
xB = float(input('X: '))
yB = float(input('Y: '))

from math import sqrt
print('Расстояние мужду А и В равно: ',round(sqrt((xA - xB)**2 + (yA - yB)**2), 2))