def mysort(a):
    '''
    element - нахождение текущего элемента в списке
    :param a: неотсортированные данные
    :return: отсортированные данные
    '''
    for i in range(len(a)):
        element = a[i][0]
        j = i
        while j > 0 and a[j - 1][0] > element:
            a[j - 1][0], a[j][0] = a[j][0], a[j - 1][0]
            j -= 1
    return a


file = open('rocket.csv', encoding='utf-8') # получение данных
array = file.readlines()
file.close()
a = array.pop(0)
array = [i.split(',') for i in array]
array = [[int(''.join(i[0].split('-'))), i[1], i[2].strip()] for i in array]
array = mysort(array) # сортировка данных
k = 0   # создание счетчика для вывода первых трех элементов
array = [[str(i[0]), i[1], i[2]] for i in array]
for i in array:
    date = f'{i[0][-2:]}.{i[0][-4:-2]}.{i[0][:-4]}'
    print(f'Сигнал с шифром {i[1]} был получен {date} и предназначается для {i[-1]}')
    k += 1
    if k == 3:
        break
