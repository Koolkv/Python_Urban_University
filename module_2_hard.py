import random

kill_nums = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
chance_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
non_kill_password_list = []
one_chance_num = random.choice(kill_nums)

print(f'Выпало число {one_chance_num}')

for i in chance_nums:
    for k in chance_nums:
        sum_i_k = i + k
        if one_chance_num % sum_i_k == 0:
            non_kill_password_list.append(i)
            non_kill_password_list.append(k)
        else:
            continue

print(*non_kill_password_list)
