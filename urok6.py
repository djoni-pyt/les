# # списки и кортежи

# # list = [1,2,3,'hello',]
# # print(list[0])

# list = [1,4,8,55]

# # add list append() в конец списка
# list.append(2)

# # в начало списка добавит индекс, значение - insert(0,5)
# list.insert(0,5)


# #delete remove() 
# # list.remove(1) 

# # index
# list.index(2)

# # delete return index 
# list.pop()

# # clear list
# # list.clear()


# # count
# # list.count()


# # copy()
# # a = []
# # a = list.copy()

# # print(a)


# # sort
# # list.sort()
# # list.sort(reverse=True)

# # reverse


# # sorted(list) копирует отсортированный список

# # delete
# # del list[0]

# print(list)

# import copy

# list = [0,2,3,1, [4,5,6,],7,8,9]
# print(list[4][0])

# полная копия 
# list2= copy.deepcopy(list)
# print(list2)

# кортежи неизменяемый 

# a = (1.2,3,4,5,)

# b,*d = (1,2,3,4,5,6,7,) 

# print(b,d)

# a = []
# for i in range(0,100,2):
#     a.append(i)
# print(a)

# sum, min, max ФУНКЦИИ

# dz

# 1
# Из введенной пользователем строки создать список. 
# Удалить из этого списка все буквы ‘a’, ‘e’, ‘u’. 
# Строка вводится на английском и символы для удаления так же на английском. 

# a = input(": ")
# b = list(a)
# c = []
# d = []
# for i in b:
#     if i == 'a' or i == 'e' or i == 'u':
#          d.append(i) 
#     else:
#         c.append(i) 
# print(c)
# print('удаленные буквы ',d)
 
# Задание №2
# Создать список, в котором N элементов 
# (N - введенное пользователем число). 
# Заполнить список целыми случайными числами от 0 до 20. Вывести получившийся результат.

# num = int(input("N: "))
# res = []
# for i in range(0, num):
#     res.append(i)
# print(res)

