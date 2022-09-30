
 #  Задание 1  Написать программу которая проверяет что в строке есть хотя бы один пробел,
 #число, буква нижнего и верхнего регистра. Если это так, то вывести 'YES', иначе 'NO'


import string

test_string = input('Введите строку: ')

symbol_space = 0
symbol_lower = 0
symbol_upper = 0
symbol_digit = 0

for symbol in test_string:
     if symbol.isspace():
         symbol_space += 1
     elif symbol.islower():
         symbol_lower += 1
     elif symbol.isupper():
         symbol_upper += 1
     elif symbol.isdigit():
         symbol_digit += 1
if symbol_lower != 0 and symbol_upper != 0 and symbol_digit != 0 and symbol_space != 0:
    print('YES')
else:
    print('NO')

