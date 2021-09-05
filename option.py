from def_root_add import *

def option_root_dir_1():
    print(OK + DEFAULT_ROOT + RESET)
    print_defis()
    print(ERROR + DEFAULT_ROOT_DIR + RESET)
    print_defis()
    print(ERROR + CTRL_C + RESET)
    print_defis()
    root_dir(input(TEXT_COLOR_INPUT + 'Укажите корневой каталог: ' + RESET))
    clearConsole()
    option_ok()


def option_add_dir_2():
    dir_txt_f = ''
    dir_txt = ''
    try:
        with open(VAR_ADD, 'r', encoding='utf-8') as f:
            dir_txt_f = [dir_txt for dir_txt in f.read().split('\n') if dir_txt]
            print(OK + 'Список файлов и каталогов для отслеживания:' + RESET)
    except:
        print_defis()
        print(ERROR + 'Список файлов и каталогов для отслеживания не найден\nВведите данные' + RESET)
        print_defis()
    finally:
        for dir_txt in dir_txt_f:
            print(dir_txt)
            print_defis()
    print(ERROR + CTRL_C + RESET)
    print_defis()
    add_directories(input(TEXT_COLOR_INPUT + 'Укажите файлы и папки для очистки: ' + RESET))
    clearConsole()
    option_ok()

