import os
import time

directory = '/Users/nikitabo/PycharmProjects/homework/module 7'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getatime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')