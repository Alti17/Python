#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#стоящих на нечётной позиции.
def sum_negative_index(list):
    s = 0
    for i in range(len(list)):
        if i % 2 != 0:
            s += list[i]
    print("Сумма элементов равна: ", s)

list = list(map(int, input("Введите числа через пробел:\n").split()))
sum_negative_index(list)