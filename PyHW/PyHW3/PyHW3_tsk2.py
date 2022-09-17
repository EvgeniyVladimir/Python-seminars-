# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = list(map(int, input('Введите число: ').split()))
# numbers = [2, 3, 4, 5, 6]
result = list()                                                    
for i in range(len(numbers)//2): 
    result.append(numbers[i] * numbers[len(numbers) - i - 1])
if len(numbers) % 2 == 1: 
    result.append(numbers[int(len(numbers)/2)] **2) 
print(*result)  