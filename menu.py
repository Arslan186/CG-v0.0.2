import sys
from core import *
from datetime import datetime
import threading
import pyfiglet
import platform
import collections
from variable import *
from general_def import *
from option import *


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
            option_root_dir_1()
        elif option == 2:
            try:
                while(True):
                    option_add_dir_2()
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
