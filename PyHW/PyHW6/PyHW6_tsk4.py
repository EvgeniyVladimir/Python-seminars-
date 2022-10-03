#Задача2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# _____________
# Было
# n = int(input('Введите число: '))
# b = 1                                   
# a = [ ]                                  
# for i in range(n): 
#     b*=(i +1)
#     a.append(b)      
# print(a)  
# _________________
# стало
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(list(map(factorial, [i for i in range(1, int(input('Введите число: '))+1)])))

# import math
# x = int(input(' Введите число: '))                     # \
# factorial = lambda x: x and x * factorial(x-1) or 1    #  > не работает
# print(factorial(x))                                    # /
