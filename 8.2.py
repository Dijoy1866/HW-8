
# Задание 2 Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.


count = int(input('Веди число: '))

f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < count:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    i += 1
print()
