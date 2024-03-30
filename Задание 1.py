file = open('rocket_part.txt', encoding='utf-8') # получение данных
array = file.readlines()
file.close()
array = [i.split() for i in array]
s, d = input(), dict()
# s - входящий запрос
# d - база данных, в которой хранятся сообщения
for i in array:
    d[i[1]] = i[5]
print(f'В {s} было получено - {d[s]} шифров')
