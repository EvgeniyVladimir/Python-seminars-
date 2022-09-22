# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

from random import randint


n = int(input('Введите число: '))
list = []
for i in range(1, n + 1):
    a = randint(-n, n + 1)
    list.append(a)
print(list)

newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)

# b = [1, 1, 2, 3, 3, 4, 5]
# a = []
# for i in b:
#     if b.count(i) == 1:
#         a.append(i)

# print(a)