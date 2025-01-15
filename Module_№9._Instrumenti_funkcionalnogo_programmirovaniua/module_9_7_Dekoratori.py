import math


def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)
        if sum_ == 1:
            print(
                "Число 1 не является ни простым, ни составным числом, так как у него только один делитель — 1")
            return sum_
        if sum_ > 1:
            if sum_ == 2 or sum_ == 3:
                print("Простое")
                return sum_
            for i in range(2, sum_):
                if sum_ % 1 == 0 and sum_ % sum_ == 0 and not sum_ % i == 0:
                    pass
                else:
                    print("Составное")
                    return sum_
            print("Простое")
            return sum_
        else:
            print("Число должно быть натуральным, то есть больше 0")
            return sum_
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
