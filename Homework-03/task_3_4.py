"""4) Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
Также, если эта центральная буква равна первой букве в строке, то создать и вывести
часть строки между первым и последним символами исходной строки. (подсказка: для получения
центральной буквы, найдите длину строки и разделите ее пополам. Для создания результирующий строки используйте срез)"""

str0 = input("Input your string: ")
str1 = str0[(len(str0) // 2)]
print(str1)

if str0[0] == str1:
    print(str0[1:-1])