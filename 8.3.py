# Задаине №3 Напишите программу где пользователь вводит пароль, а программа проверяет сложность
# пароля и выводит свой результат в оценочной шкале от 1 до 5.


import string

password = input('Введите пароль: ')

upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
special = any([1 if i in string.punctuation else 0 for i in password])
digits = any([1 if i in string.digits else 0 for i in password])
length = len(password)

if length >= 8:
    length = True
else:
    length = False

characters =[upper_case, lower_case, special, digits, length]

score = 0

for i in range(len(characters)):
    if characters[i]:
        score += 1

print('Надежность пароля: %s из 5' % score)
