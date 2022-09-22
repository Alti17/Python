#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def multiplication(array):
    r = len(array)//2  
    new_array = [array[i]*array[len(array)-i-1] for i in range(r)]
    print(new_array)

array = list(map(int, input("Введите числа через пробел:\n").split()))
multiplication(array)