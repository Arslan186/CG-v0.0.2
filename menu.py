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


def print_defis():
    print('{:^10s}'.format(DEFIS_COLOR + DEFIS + RESET))


def figlet():
    CG = pyfiglet.figlet_format("C|G", font = "isometric3")
    print(CG)


def print_platform():
    print("{:%Y-%m-%d %H:%M}".format(datetime.now()))
    PUNAME = platform.uname()
    print_defis()
    print('OS - {0[0]}\nАрхитектура - {0[4]}'.format(PUNAME))


def print_menu():
    figlet()
    print_platform()
    print_defis()
    print('{:^65s}'.format(TEXT_COLOR + 'Главное меню' + RESET))
    for key in MENU_OPTIONS.keys():
        print_defis()
        print('{:>5} {:>3} {:>2} {:>2}'.format('|',key, '---', MENU_OPTIONS[key]))


def option_ok():
    print(OK + 'Выполнено' + RESET)


def option1():
    print(OK + 'По умолчанию корневой каталог на андроид устройствах:' + RESET)
    print(ERROR + '/data/data/com.termux/files/home/storage/shared' + RESET)
    root_dir(input(TEXT_COLOR_INPUT + 'Укажите корневой каталог: ' + RESET))
    option_ok()


def option2():
    print(OK + 'Список файлов и каталогов для отслеживания:' + RESET)
    with open('add_dir.txt', 'r', encoding='utf-8') as dir_txt_f:
        dir_txt = ''
        for dir_txt in dir_txt_f:
            print(dir_txt)
    print(ERROR + 'Для возврата в предыдущее меню используйте Ctrl+C' + RESET)
    add_directories(input(TEXT_COLOR_INPUT + 'Укажите файлы и папки для очистки: ' + RESET))
    option_ok()


def option3():
    delet_file_dir()


def menu_start():
    while(True):
        print_menu()
        option = ''
        print_defis()
        try:
            option = int(input(TEXT_COLOR_INPUT + 'Введите команду: ' + RESET))
        except:
            print(ERROR + 'Вы ввели не число' + RESET)
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
            print(ERROR + 'Неверная команда, введите число от 1 до 4' + RESET)

if __name__=='__main__':
    menu_start()
