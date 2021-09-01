import sys
from core import *
from datetime import datetime
import threading
import pyfiglet
import platform
import collections
from variable import *
from add_directories import *
from root_dir import *

MENU_OPTIONS = {
    1: 'Укажите корневой каталог',
    2: 'Укажите файлы и папки для очистки',
    3: 'Очистить',
    4: 'Выход',
}


def print_defis():
    print('{:^10s}'.format(DEFIS))


def figlet():
    CG = pyfiglet.figlet_format("C|G", font = "isometric3")
    print(CG)


def print_platform():
    print("{:%Y-%m-%d %H:%M}".format(datetime.now()))
    PUNAME = platform.uname()
    print_defis()
    print('OS - {0[0]}\nАрхитектура - {0[4]}'.format(PUNAME))
    print_defis()


def print_menu():
    figlet()
    print_platform()
    print_defis()
    print('{:^55s}'.format('Главное меню'))
    for key in MENU_OPTIONS.keys():
        print_defis()
        print('{:>5} {:>3} {:>2} {:>2}'.format('|',key, '---', MENU_OPTIONS[key]))


def option_ok():
    print('Выполнено')


def option1():
    print('По умолчанию корневой каталог на андроид устройствах:')
    print('/data/data/com.termux/files/home/storage/shared')
    root_dir(input('Укажите корневой каталог: '))
    option_ok()


def option2():
    print('Список файлов и каталогов для отслеживания:')
    with open('add_dir.txt', 'r', encoding='utf-8') as dir_txt_f:
        dir_txt = ''
        for dir_txt in dir_txt_f:
            print(dir_txt)
    print('Для возврата в предыдущее меню используйте Ctrl+C')
    add_directories(input('Укажите файлы и папки для очистки: '))
    option_ok()


def option3():
    delet_file_dir()
    option_ok()


def menu_start():
    while(True):
        print_menu()
        option = ''
        print_defis()
        try:
            option = int(input('Введите команду: '))
        except:
            print('error')
        #Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            try:
                while(True):
                    option2()
            except KeyboardInterrupt:
                pass
        elif option == 3:
            option3()
            exit()
        elif option == 4:
            exit()
        else:
            print('Неверная команда, введите число от 1 до 4')

if __name__=='__main__':
    menu_start()
