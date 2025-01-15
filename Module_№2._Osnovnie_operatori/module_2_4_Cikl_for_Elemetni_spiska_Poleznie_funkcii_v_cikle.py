numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True
    for j in range(numbers[0], numbers[i]):
        if numbers[i] % numbers[j] == 0 and numbers[i] // numbers[j] != 1:
            is_prime = False
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(f"Простые числа: {primes}")
print(f"Сложные числа: {not_primes}")