numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True # trebuetsja raz'jasnenija na temu flagov, dlja menja tema ne raskrita
for i in numbers:
    num = 0
    if i == 1: # 1 - ne prostoe i ne sostavnoe chislo
        print('it is number one, not bad')
    else:
        for k in range(2, i + 1):
            if i == 2: # 2 - prostoe chislo
                primes.append(i)
            if i != 2 and i % k == 0:
                num += 1
            if num >= 2:
                not_primes.append(i)
                break
    if num == 1:
        primes.append(i)

print(primes)
print(not_primes)