# Словари и множества
# slovar = {
#     'day': 'Monday',
#     'time':'Night',
# }
# slovar1 =dict(day='Monday', time='Night')
# lis = [[ 'day','Monday'],['time','Night',]]
# slovar2 = dict(lis)
# print(slovar)
# print(slovar1)
# print(slovar2)

# lis = [[ 'day','Monday'],['time','Night',]]
# slovar2 = dict(lis)
# print(slovar2['day'])
# print(slovar2.get('time'))

# add slovar
# slovar = {
#     'day': 'Monday',
#     'time':'Night',
# }
# slovar['season'] = 'summer'
# print(slovar)

# slovar1={
#     1:100,
#     2:200
# }
# # methods

# # keys
# print(slovar.keys())
# sp =list(slovar.keys())
# print(sp)

# # values
# print(slovar.values())
# sp2 = list(slovar.values())
# print(sp2)

# # items
# print(slovar.items())

# # update
# slovar.update(slovar1)
# print(slovar)

# # del
# del slovar1[2]
# print(slovar1)

# st = 'hello my world'
# slovar2 = {i: st.count(i) for i in st}
# print(slovar2)

# mnogestva
# mn = {12,11,22,3,11}
# mn1 = set([1,2,3,4,4,5,5,6])
# # объединить множества  
# c = mn | mn1
# print(c)
# # объединить множества  
# d = mn.union(mn1)
# print(d)
# # & ... - пересечение.
# e = mn & mn1
# print(e)

# l = mn.difference(mn1)
# print(l)

# # add in mnogestva
# mn.add(5461)

# # remove
# mn.remove(1)

# -----------------------------------------------------------
# dz

# Задание №1
# Создать Русско-Английский словарь, который содержит 10 слов с переводом. В качестве ключа используются русские слова.
# Например:
# "кот" : "cat"
# "мышь" : "mouse"
# "собака" : "dog"
# "животные": "animals"
# Остальное дополнить самостоятельно.
# Пользователь вводит русское слово, нео ходимо найти в словаре его перевод и вывести на экран. Вывод должен иметь вид:
# Слово ХХХХХХ переводится как: YYYYYY.

# world = input(": ")

# slovar = {
# "кот" : "cat",
# "мышь" : "mouse",
# "собака" : "dog",
# "животные": "animals",
# }

# if world in slovar.keys():
#     print(f'Слово {world} переводится как: {slovar[world]}.')
# else:
#     print("net takogo slova")