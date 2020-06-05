import sys
import os
import os.path
from pathlib import Path
import shutil
print(sys.platform)


#Добавить путь для удаления папок
def write_way(text=None):
    with open('way.txt', 'w', encoding='utf-8' ) as f:
        if text:
            f.write(text)


#Добавить дириктррии для удаления
def write_dir_del_folder(text=None):
    with open('dir_del.txt', 'w', encoding='utf-8') as f:
        if text:
            f.writelines(text)


#Склеить строку пути и дирикторий
def way_create():
    with open('way.txt', 'r', encoding='utf-8') as f:
        for line_w in f:
            result_w = line_w
    with open('dir_del.txt', 'r', encoding='utf-8') as f:
        for line_d in f:
            result_d = line_d.replace('\n', '')
            result_dir = os.path.join(result_w, result_d)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), result_dir)
            shutil.rmtree(path, ignore_errors=True)


#Смена дириктории
def change_dir(name):
    result = os.chdir(name)
    print(os.getcwd())

#Удаление дирикторий

if __name__ == '__main__':
    #write_dir_del_folder('test1\n' 'test2\n' 'test3\n')
    #write_way('/storage/shared/')
    way_create()
