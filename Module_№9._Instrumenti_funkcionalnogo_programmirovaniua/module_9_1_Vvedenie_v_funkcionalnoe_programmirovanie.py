def apply_all_func(int_list, *functions):
    result = {}
    for i in int_list:
        if isinstance(i, str):
            return None
    for func in functions:
        result[func.__name__] = func(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# print(apply_all_func([100, 6, 20, 15, 9, -5], max, min))
# print(apply_all_func([100, 6, 20, 15, 9, -5], len, sum, sorted))
# print(apply_all_func([100, 6, 20, 15, 9, -5], min, max, sum, len, sorted))
# print()
# print(apply_all_func([100, 6, 20, "True", 15, 9, -5], max, min))
# print(apply_all_func([100, 6, 20, "3", 15, 9, -5], len, sum, sorted))
# print(apply_all_func([100, 6, 20, " ", 15, 9, -5], min, max, sum, len, sorted))
# print()
# print(apply_all_func([100, 6, False, 20, 15, 9, -5], min, max, sum, len, sorted))
# print(apply_all_func([100, 6, True, 20, 15, 9, -5], min, max, sum, len, sorted))
