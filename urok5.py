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
# print(stroka.replace(' ', ' * '))

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

st = input(': ')
st2 = st.lower()
a = 0
o = 0
for i in st2:
    if i == 'a':
        a+=1
    elif i == 'o':
        o+=1
print(f'Буква a встречается {a} раз')
print('=========================================')
print(f'Буква o встречается {o} раз')        