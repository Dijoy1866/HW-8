# Задаине №3 Напишите программу где пользователь вводит пароль, а программа проверяет сложность
# пароля и выводит свой результат в оценочной шкале от 1 до 5.


lower_case = 0
upper_case = 0
special = 0
digits = 0
password = input('Введите пароль на проверку: ')

if password == 'qwerty' or password == 'admin' or password == '':
    print('Оценка сложности пароля -', 1)
    exit()

for i in range(len(password)):
    if str(password[i]).islower():
        lower_case += 1
    elif str(password[i]).isupper():
        upper_case += 1
    elif str(password[i]).isnumeric():
        digits += 1
    else:
        special += 1

if lower_case == len(password) or upper_case == len(password) or digits == len(password) or special == len(
        password):
    print('Оценка сложности пароля -', 2)

elif lower_case > 0 and digits > 0 and upper_case == 0 and special == 0:
    print('Оценка безопастности пароля -', 3)
elif lower_case > 0 and upper_case > 0 and digits == 0 and special == 0:
    print('Оценка сложности пароля -', 3)
elif lower_case > 0 and special > 0 and digits == 0 and upper_case == 0:
    print('Оценка сложности пароля -', 3)
elif upper_case > 0 and special > 0 and digits == 0 and lower_case == 0:
    print('Оценка сложности пароля -', 3)
elif upper_case > 0 and digits > 0 and special == 0 and lower_case == 0:
    print('Оценка сложности пароля -', 3)
elif special > 0 and digits > 0 and upper_case == 0 and lower_case == 0:
    print('Оценка сложности пароля -', 3)

elif lower_case > 0 and digits > 0 and upper_case > 0 and special == 0:
    print('Оценка сложности пароля -', 4)
elif special > 0 and digits > 0 and upper_case > 0 and lower_case == 0:
    print('Оценка сложности пароля -', 4)
elif lower_case > 0 and digits > 0 and special > 0 and upper_case == 0:
    print('Оценка сложности пароля -', 4)
elif lower_case > 0 and special > 0 and upper_case > 0 and digits == 0:
    print('Оценка сложности пароля -', 4)

elif lower_case > 0 and digits > 0 and upper_case > 0 and special > 0 and len(password) > 8:
    print('Оценка сложности пароля -', 5)


