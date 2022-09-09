#Реализуйте алгоритм перемешивания списка.
list = [int(i) for i in input('Введите значения: ').split()]
print(list) 
import random
random.shuffle(list)
print(list)