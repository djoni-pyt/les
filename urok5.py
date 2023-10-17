# # Работа со строками 

# stroka = 'helLo, hello, HELLO'
# # print(stroka[1:4:2])

# # revers
# # print(stroka[::-1])

# # capitalize()
# print(stroka.capitalize())

# # upper()
# print(stroka.upper())

# # lower
# print(stroka.lower())

# # swapcase()
# print(stroka.swapcase())

# # join()
# raz = '-/'
# res = raz.join('fvrtfrdddddrd')
# print(res)

# # split
# print(stroka.split('e'))

# # replace()
# # print(stroka.replace(' ', ' * '))
#  Мы можем использовать replace(), чтобы удалить все пробелы из строки. Эта функция также удалит пробелы между словами.

# # len
# print(len(stroka))

# dz

# Задание №1
# Дана строка, введенная пользователем, состоящая из двух слов, разделенных пробелом.
# Переставить эти слова местами, записать в строку и вывести её на экран.

# st = input("Напишите 2 слова: ")
# res =st.split(' ')
# print(''.join(res[::-1]))

# Задание №2
# Пользователь вводит строку, необходимо посчитать сколько в этой строке встречается букв "a" и "o" .
# Предварительно необходимо перевести строку в нижний регистр. Ввод и проверки осуществляются на английском языке.

# st = input(': ')
# st2 = st.lower()
# a = 0
# o = 0
# for i in st2:
#     if i == 'a':
#         a+=1
#     elif i == 'o':
#         o+=1
# print(f'Буква a встречается {a} раз')
# print('=========================================')
# print(f'Буква o встречается {o} раз')        

# Задание №3
# Написать программу, которая подсчитывает, сколько содержится цифр в введенной пользователем строке.

# st = input("numb: ")

# for i in st:
#       print(len(i))

# n = int(input("Введите число:"))
# count = 0.
# while(n > 0):
#     count = count + 1.
#     n = n // 10.
# print("Количество цифр равно:", count)

# Задание №5
# В введенной пользователем строке изменить регистр букв на противоположный и удалить все пробелы.

# st = input("TEXT: ")
# if st ==st.upper():
#     print(st.lower())
# elif st == st.lower():
#     print(st.upper())

# 2

st = input("TEXT: ")
# for i in st:
#     if i == i.upper():
#         print(i.lower())
#     elif i == i.lower():
#         print(i.upper())
print(st.swapcase().replace(' ', ''))
