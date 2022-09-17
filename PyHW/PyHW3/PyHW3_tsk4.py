# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

denary = int(input('Введите десятичное число: '))  
binary= ' '  
while denary > 0:  
    binary = str(denary %2 ) + binary  
    denary = denary // 2  
print('Двоичное число: ' + binary)  

# num = int(input('Введите десятичное число: '))
# print(f'{num:b}')