from time import sleep
from datetime import datetime
from threading import Thread

time_start = 0
time_end = 0


def vremua_izmeritel(flag=False):
    global time_start, time_end
    if not flag:
        time_start = datetime.now()
        return None
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)


vremua_izmeritel()


def write_words(word_count, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i+1} \n")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

vremua_izmeritel(True)
vremua_izmeritel()

thr_first = Thread(target=write_words, args=(10, "example5.txt"))
thr_secod = Thread(target=write_words, args=(30, "example6.txt"))
thr_third = Thread(target=write_words, args=(200, "example7.txt"))
thr_fourth = Thread(target=write_words, args=(100, "example8.txt"))
thr_first.start()
thr_secod.start()
thr_third.start()
thr_fourth.start()
thr_first.join()
thr_secod.join()
thr_third.join()
thr_fourth.join()
vremua_izmeritel(True)
