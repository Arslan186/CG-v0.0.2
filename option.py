from variable import *
from root_dir import *
from add_directories import *


def option_ok():
    print(OK + 'Выполнено' + RESET)


def option_root_dir_1():
    print(OK + 'По умолчанию корневой каталог на андроид устройствах:' + RESET)
    print(ERROR + '/data/data/com.termux/files/home/storage/shared' + RESET)
    root_dir(input(TEXT_COLOR_INPUT + 'Укажите корневой каталог: ' + RESET))
    option_ok()


def option_add_dir_2():
    print(OK + 'Список файлов и каталогов для отслеживания:' + RESET)
    with open('add_dir.txt', 'r', encoding='utf-8') as dir_txt_f:
        dir_txt = ''
        for dir_txt in dir_txt_f:
            print(dir_txt)
    print(ERROR + 'Для возврата в предыдущее меню используйте Ctrl+C' + RESET)
    add_directories(input(TEXT_COLOR_INPUT + 'Укажите файлы и папки для очистки: ' + RESET))
    option_ok()
            
