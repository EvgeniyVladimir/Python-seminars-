# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# _________
# Было

# my_text = 'Напиабв Напишите абв програбвмму программу, удаляющую из \
#     этого абв текст текстаабв все вабвсе слова, содерабващие содержащие "абв"'
# rem_txt = input('введите текст для удаления: ')
# def del_some_words(my_text):
#     my_text = list(filter(lambda x: rem_txt not in x, my_text.split()))
#     return " ".join(my_text)
# my_text = del_some_words(my_text)
# print(my_text)

# ______________
# Стало

inp = list(map(str, input('введите текст: ').split()))
rem_txt = input('введите текст для удаления: ')
print(*list(filter(lambda x: rem_txt not in x, inp)))
