def impo(some_person):
    with open('info.txt', 'a', encoding='utf-8') as f:
        f.write(some_person + '\n')
        # if len(info.split()) == 1:
        #     f.write(f'экспорт - {info}' + '\n')