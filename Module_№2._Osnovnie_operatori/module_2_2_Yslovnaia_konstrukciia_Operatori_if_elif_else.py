first = int(input("Введите целое число: "))
second = int(input("Введите целое число: "))
third = int(input("Введите целое число: "))
if first == second and second == third:
    print(3)
elif first == second or first == third:
    print(2)
elif second == first or second == third:
    print(2)
elif third == first or third == second:
    print(2)
else:
    print(0)