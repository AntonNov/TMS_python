"""3) Ввести строку. Если длина строки больше 10 символов, то создать новую строку с 3 восклицательными знаками в конце
('!!!') и вывести на экран. Если меньше 10, то вывести на экран второй символ строки"""

str0 = input("Input your string: ")

if len(str0) > 10:
    print("!!!")
elif len(str0) < 10:
    print("Второй символ строки:", str0[1])
