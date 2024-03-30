file = open('rocket.csv', encoding='utf-8') # получение данных
array = file.readlines()
file.close()
a = array.pop(0)
array = [i.split(',') for i in array]
array = [[''.join(i[0].split('-')), i[1], i[2].strip()] for i in array]
array = [[f'{i[0][:-4]}-{i[0][-4:-2]}-{i[0][-2:]}', i[1], i[2]] for i in array]
d = dict() # создание базы данных
for i in array:
    d[i[0]] = [i[1], i[2]]
s = input()
while s != 'sleep': # обработка запросов
    if s in d:
        print(f'Шифр: {d[s][0]} от: {d[s][1]} был получен {s}')
    else:
        print('в этот день космос молчал')
    s = input()
