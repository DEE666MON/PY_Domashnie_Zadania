import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, "r", encoding='utf-8') as file:
        if file.readline() != '':
            all_data.append(file.read())


filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов


# time_start = datetime.now()
# for fn in filenames:
#     read_info(fn)
# time_end = datetime.now()
# time_res = time_end - time_start
# print(time_res)

# Время - 0:00:00.656606

# Многопроцессный


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time_start = datetime.now()
        pool.map(read_info, filenames)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)

# Время - 0:00:00.357324
