# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.
# ________
# Было
# from random import randint
# n = int(input('Введите число: '))
# list = []
# for i in range(1, n + 1):
#     a = randint(-n, n + 1)
#     list.append(a)
# print(list)
# ___________
# Стало
numbers = list(map(int, input('Введите числа: ').split()))
print(*list(filter(lambda x: numbers.count(x) == 1, numbers)))