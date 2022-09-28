# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def Compression(text): #алгоритм сжатия
    compresdata = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compresdata += str(count) + text[i]
        i += 1
    return compresdata
def Recovery(text): #алгоритм восстановления
    datarecovery = ''
    i = 0
    while i < len(text):
        datarecovery += str(text[i+1]) * int(text[i])
        i+=2
    return datarecovery
with open('Text1.txt', 'r') as t1:
    t1 = t1.read()
with open('Text2.txt', 'w+') as t2:
    t2.write(Compression(t1))
    t2.seek(0) #возврат курсора на начало строки
    t2 = t2.read()
with open('Text3.txt', 'w') as t3:
    t3.write(Recovery(t2))
print(f'текст после кодировки: {t2}')
print(f'текст после расшифровки: {t3}')

# ___________________

# with open('decoded.txt', 'r') as data:
#     my_text = data.read()

# def encode(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code
            
# str_code = encode(my_text)
# print(f'текст после кодировки: {str_code}')

# with open('encoded.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding(ss):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding(my_text2)
# print(f'текст после расшифровки: {str_decode}')

# _______________________________________________
