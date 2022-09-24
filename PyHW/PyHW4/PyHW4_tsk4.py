# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите степень k: '))
koefs = list()
for i in range(1, k + 2):
  koefs.append(randint(1, 100))

ans = list()
for i in range(len(koefs)):
  if k == 1:
    ans.append(f'{koefs[i]}*x')
  elif k == 0:
    ans.append(f'{koefs[i]}')
  else:
    ans.append(f'{koefs[i]}*x**{k}')
  flag = randint(0, 1)
  if flag == 1:
    ans.append('+')
  elif flag == 0:
    ans.append('-')
  k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()
# ______________________

# import random as r

# def form_funk(num, some_str):
#     if num == 1:
#         a = r.randint(0, 100)
#         b = r.randint(0, 100)
#         if a == 1 and b > 0:
#             some_str += 'x+' + str(b)
#         if a == 1 and b == 0:
#             some_str += 'x'
#         if a == 0:
#             some_str += str(b)
#         if a > 1:
#             some_str += str(a) + 'x+' + str(b)
#         if a == 0 and b == 0:
#             return some_str
#         return some_str
#     else:
#         a = r.randint(0, 100)
#         if a == 1:
#             some_str += 'x' + '^' + str(num) + '+' + form_funk(num-1, some_str)
#         if a == 0:
#             some_str += form_funk(num-1, some_str)
#         if a > 1:
#             some_str += str(a) + 'x' + '^' + str(num) + \
#                 '+' + form_funk(num-1, some_str)
#         return some_str


# some_str = ''
# number = int(input('введите степень : '))
# print(form_funk(number, some_str) + ' = 0')

# ______________________________________________________________

# from random import randint

# print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
# k = int(input("Введите степень k: "))

# factor = []
# for i in range(1, k +2):
#     factor.append(randint(1, 100))

# result = []
# for i in range(len(factor)):
#     if k == 1:
#         result.append(f'{factor[i]}*x')
#     elif k == 0:
#         result.append(f'{factor[i]}')
#     else:
#         result.append(f'{factor[i]}*x^{k}')
#     signs = randint(0, 1)
#     if signs == 1:
#         result.append('+')
#     elif signs == 0:    
#         result.append('-')
#     k -= 1

# result.pop(-1)
# result.append('=0')

# record = open('data.txt', 'w')
# record.write(''.join(result))
# record.close()

# _______________________________________________