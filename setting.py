import os
import os.path
import shutil
from colored import fg, bg, attr
import sys
from datetime import datetime
import pyfiglet
import platform
import collections

#Variable COLOR
ERROR = bg(196)
OK = bg(26) + fg(52)
DEFIS_COLOR = fg(88)
TEXT_COLOR = fg(0)
TEXT_COLOR_INPUT = bg(34) + fg(0)
TEXT_COLOR_DIR = bg(240) + fg(0)
RESET = attr(0)

#Variable function menu
DEFIS = '--------------------------------------------------------'

MENU_OPTIONS = {
        1: 'Укажите корневой каталог',
        2: 'Укажите файлы и папки для очистки',
        3: 'Очистить',
        4: 'Выход',
        }

#Variable function root_dir & add_directories
VAR_ROOT = '/data/data/com.termux/files/home/CG-v0.2.0/root_dir.txt'
VAR_ADD = '/data/data/com.termux/files/home/CG-v0.2.0/add_dir.txt'

#Variable functions option
DEFAULT_ROOT = 'По умолчанию корневой каталог на андроид устройствах'
DEFAULT_ROOT_DIR = '/data/data/com.termux/files/home/storage/shared'
CTRL_C = 'Для возврата в предыдущее меню используйте Ctrl+C'


#General function
def print_defis():
    print('{:^10s}'.format(DEFIS_COLOR + DEFIS + RESET))


def option_ok():
    print(OK + 'Выполнено' + RESET)
    print_defis()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
