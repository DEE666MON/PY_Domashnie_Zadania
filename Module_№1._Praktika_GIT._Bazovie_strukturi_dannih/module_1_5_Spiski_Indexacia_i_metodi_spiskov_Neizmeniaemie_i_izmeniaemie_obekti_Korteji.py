immutable_var = (1, 1.1, "Привет")
print(immutable_var)
# immutable_var[2] = 2 # - нельзя изменить, так как это неизменяемый список(Кортеж), если бы был внутри кортежа список([1, 2], 3), то можно было бы изменить в квадратных скобках
# print(immutable_var)
mutable_list = [1, 1.1, "Привет"]
mutable_list = ["Привет", 1.1, 1]
print(mutable_list)