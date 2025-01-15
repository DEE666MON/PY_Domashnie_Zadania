my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ml_count = 0
while ml_count < len(my_list):
    if my_list[ml_count] < 0:
        break
    if my_list[ml_count] == 0:
        ml_count += 1
        continue
    print(my_list[ml_count])
    ml_count += 1