# Задание №4 Напишите программу где пользователь вводит число symbol_len, а программа генерирует
# пароль длинной symbol_len. Чем выше будет сложность пароля, тем лучше. Сложность пароля буду
# оценивать по шкале от 1 до 5 из задании #3
#
# ГОТОВО

import random
import string

symbol_len = int(input('Длина пароля:'))

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special = '()[]{}@# %^&*_+-='
digits = '0123456789'

all = lower_case + upper_case + special + digits
passworld = ''.join(random.sample(all, symbol_len))


upper_case = any([1 if i in string.ascii_uppercase else 0 for i in passworld])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in passworld])
special = any([1 if i in string.punctuation else 0 for i in passworld])
digits = any([1 if i in string.digits else 0 for i in passworld])
length = symbol_len

if length >= 8:
    length = True
else:
    length = False

characters = [upper_case, lower_case, special, digits, length]

score = 0

for i in range(len(characters)):
    if characters[i]:
        score += 1

print('Надежность пароля: %s из 5' % score)

print('Ваш пaроль: ' + passworld)

