import random

one_chance_num = random.choice(range(3, 21))  # случайное число из списка от 3 до 20
non_kill_password_list = ''  # числа для подбора пароля
skip_num = []

print(f'Выпало число {one_chance_num}')

for i in range(1, one_chance_num):  # берем первое число из диапозона
    if i in skip_num:
        continue
    skip_num.append(i)
    for k in range(i + 1, one_chance_num):  # берем вотрое число из диапозона и начинаем работать с первым
        if one_chance_num % (i + k) == 0:  # проверка деления суммы двух чисел
            non_kill_password_list += str(i)  # запихиваем первое число в список
            non_kill_password_list += str(k)  # запихиваем второе число в список
        else:
            continue

print(f'пароль: {non_kill_password_list}')

# import random
#
# kill_nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# chance_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# non_kill_password_list = []  # список чисел для подбора пароля
# one_chance_num = random.choice(kill_nums)  # случайное число из списка от 3 до 20
#
# print(f'Выпало число {one_chance_num}')
#
# for i in chance_nums:  # берем первое число из списка
#     for k in chance_nums:  # берем вотрое число из списка и начинаем работать с первым
#         sum_i_k = i + k  # сумма первого числа и второго
#         if one_chance_num % sum_i_k == 0:  # проверка деления суммы двух чисел
#             non_kill_password_list.append(i)  # запихиваем первое число в список
#             non_kill_password_list.append(k)  # запихиваем второе число в список
#         else:
#             continue
#
# print(*non_kill_password_list)
