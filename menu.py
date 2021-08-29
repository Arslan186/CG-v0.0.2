import sys
from core import write_dir_del_folder, write_way, delet
from termcolor import colored
from datetime import datetime
import threading
import pyfiglet
import platform
import collections


MENU_OPTIONS = {
    1: 'Укажите корневой каталог',
    2: 'Укажите файлы и папки для очистки',
    3: 'Очистить',
    4: 'Выход',
}

DEFIS = '--------------------------------------------------------'


def print_defis():
    print(colored('{:^10s}'.format(DEFIS, 'grey')))


def figlet():
    CG = pyfiglet.figlet_format("C|G", font = "isometric3")
    print(colored(CG, 'magenta'))


def print_platform():
    print(colored("{:%Y-%m-%d %H:%M}".format(datetime.now()), 'grey'))
    PUNAME = platform.uname()
    print_defis()
    print(colored('OS - {0[0]}\nАрхитектура - {0[4]}'.format(PUNAME), 'magenta'))
    print_defis()



def print_menu():
    figlet()
    print_platform()
    print(colored('серый', 'grey'))
    print(colored('красный', 'red'))
    print(colored('зеленый', 'green'))
    print(colored('желтый', 'yellow'))
    print(colored('синий', 'blue'))
    print(colored('пурпурный', 'magenta'))
    print(colored('голубой', 'cyan'))
    print(colored('белый', 'white'))

    print_defis()
    print(colored('{:^55s}'.format('Главное меню'), 'green'))
    for key in MENU_OPTIONS.keys():
        print_defis()
        print(colored('{:>5} {:>3} {:>2} {:>2}'.format('|',key, '---', MENU_OPTIONS[key]),'blue'))


def option_ok():
    print(colored('Выполнено', 'magenta'))


def option1():
    print(colored('По умолчанию корневой каталог на андроид устройствах:', 'grey'))
    print(colored('/data/data/com.termux/files/home/storage/shared', 'magenta'))
    write_way(input(colored('Укажите корневой каталог: ', 'green')))
    option_ok()

def option2():
    print(colored('Для возврата в предыдущее меню используйте Ctrl+C', 'grey'))
    write_dir_del_folder(input(colored('Укажите файлы и папки для очистки: ', 'green')))
    option_ok()

def option3():
    delet()
    option_ok()


def menu_start():
    while(True):
        print_menu()
        option = ''
        print_defis()
        try:
            option = int(input(colored('Введите команду: ', 'green')))
        except:
            print('error')
        #Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            try:
                while(True):
                    option2()
                    print('ok')
            except KeyboardInterrupt:
                pass
        elif option == 3:
            option3()
            exit()
        elif option == 4:
            print(colored('Спасибо что пользуютесь нашим программным обечпечением', 'red'))
            exit()
        else:
            print(colored('Неверная команда, введите число от 1 до 4', 'red'))

if __name__=='__main__':
    menu_start()
