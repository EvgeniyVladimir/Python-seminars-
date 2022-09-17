# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# numbers = list(map(int, input('Введите число: ').split()))
numbers = [1.1, 1.2, 3.1, 5, 10.01]
result = list()                                                    
for i in numbers: 
    x = i - int(i)
    if x !=0:
        result.append(round(x, 5))
if max(result) == min(result):
    print(max(result))
else:
    print(max(result) - min(result))