# # 3 urok
# # цикл
# # x = 1
# # c = 1
# # while x < 0:
# #     c = c * x
# # x =int(input())
# # if x >= 10:
# #     print(x, '>= 10')
# # else:
# #     print(x, '< 10')

# # Логические операторы and,or,not

# # n = int(input())

# # if n == 10 or n == 14 or n == 30:
# #     print(n)

# # elif(n > 100) and (n < 150):
# #     print("100 and 150")

# # else:
# #     print('not ')

# # x = 0
# # while x < 10:
# #     print(x)
# #     x += 1

# # Задание №1
# # Определить наибольшее и наименьшее из трех чисел, введенных пользователем.
# # a = int(input("num1: "))
# # b = int(input("num2: "))
# # c = int(input("num3: "))

# # if a < b or a < c:
# #     print(a, 'меньшее')
# # elif a > b or a > c:
# #     print(a, 'найбольшее')

# # if b < a or b < c:
# #     print(b, 'меньшее')
# # elif b > a or b > c:
# #     print(b, 'найбольшее')

# # if c < b or c < a:
# #     print(c, 'меньшее')
# # elif c > b or c > a:
# #     print(c, 'найбольшее')


# # 2
# print("Запрашиваем у пользователя месяц его рождения в формате от 1 до 12")
# qwestions = int(input(": "))

# if qwestions == 1 or qwestions == 2 or qwestions == 12:
#     print("Вы родились зимой")
# elif qwestions == 3 or qwestions == 4 or qwestions == 5:
#     print("Вы родились весной")
# elif qwestions == 6 or qwestions == 7 or qwestions == 8:
#     print("Вы родились летом")    
# elif qwestions == 9 or qwestions == 10 or qwestions == 11:
#     # print("Вы родились осенью")    
# else:
#     print("Повторите")   