import os
import time


directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = root
        filetime = os.stat(file).st_mtime
        formatted_time = time.strftime(
            "%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.getcwd()
        print(f'Обнаружен файл: {file}, \nПуть: {parent_dir+filepath[1:]}\\{file}, \nРазмер: {filesize} байт, \nВремя изменения: {formatted_time}, \nРодительская директория: {parent_dir}\n')
