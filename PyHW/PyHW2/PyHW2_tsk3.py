# 3.Задайте список из N чисел последовательности (1+1/N)^N и выведите на экран их сумму.
N = int(input('Введите число: '))
ans = list()

sum = 0
for i in range(1, N+1):
    sum = int(sum + round((1+1/i)**i, 2))
    ans.append(sum)
print(f'if N = {N}, then ansver is: {list(enumerate(ans, start = 1))}')
