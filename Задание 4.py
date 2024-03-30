def code(a):
    '''
    s1 - 1 часть кода
    s2 - 2 часть кода
    s3 - 3 часть кода
    :param a: данные, для которых создается код
    :return: код, необходимый каждому сообщению
    '''
    s3 = str(2024 - int(a[0][:-6]) - 1)
    s1 = a[2].split()
    if len(s1) == 3:
        s1 = s1[0][0] + s1[1][0].upper() + s1[2][0].upper()
    elif len(s1) == 2:
        s1 = s1[0][0] + s1[1][0].upper()
    else:
        s1 = s1[0][0]
    a1, a2, a3 = '', '', ''
    for i in a[1]:
        if i in '0123456789':
            a1 += i
        elif i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            a2 += i
        elif i in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ':
            a3 += i
    s2 = a1 + a2 + a3
    return f'{s1} {s2} {s3}'

file = open('rocket.csv', encoding='utf-8') # получение данных
array = file.readlines()
file.close()
array.pop(0)
array = [i.split(',') for i in array]
array = [[''.join(i[0].split('-')), i[1], i[2].strip()] for i in array]
array = [[f'{i[0][:-4]}-{i[0][-4:-2]}-{i[0][-2:]}', i[1], i[2]] for i in array]
code(array[0])
for i in array:
    i.append(code(i))
f = open('rocket_commands.csv', 'w', encoding='utf-8') # запись данных
for i in array:
    f.write(f'{i[0]},{i[1]},{i[2]},{i[3]}')
    f.write('\n')
