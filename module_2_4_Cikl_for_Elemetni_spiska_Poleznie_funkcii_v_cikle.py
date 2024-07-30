numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    for j in range(1,numbers[i]):
        is_prime = True
        if numbers[i] % numbers[j] == 0 and numbers[i] // numbers[j] != 1:
            is_prime = False
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
primes = set(primes)
not_primes = set(not_primes)
primes = list(primes)
not_primes = list(not_primes)
primes.sort()
not_primes.sort()
print(f"Простые числа: {primes}")
print(f"Сложные числа: {not_primes}")