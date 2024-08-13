import random

kill_nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
chance_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
non_kill_password_list = []  # список чисел для подбора пароля
one_chance_num = random.choice(kill_nums)  # случайное число из списка от 3 до 20

print(f'Выпало число {one_chance_num}')

for i in chance_nums:  # берем первое число из списка
    for k in chance_nums:  # берем вотрое число из списка и начинаем работать с первым
        sum_i_k = i + k  # сумма первого числа и второго
        if one_chance_num % sum_i_k == 0:  # проверка деления суммы двух чисел
            non_kill_password_list.append(i)  # запихиваем первое число в список
            non_kill_password_list.append(k)  # запихиваем второе число в список
        else:
            continue

print(*non_kill_password_list)
