# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Напиабв Напишите абв програбвмму программу, удаляющую из \
    этого абв текст текстаабв все вабвсе слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)
my_text = del_some_words(my_text)
print(my_text)

# from encodings import utf_8

# with open("words.txt", encoding='utf_8') as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if 'абв' in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)
