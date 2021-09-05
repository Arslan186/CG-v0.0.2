from setting import *


#Добавить корневой путь для очистки
def root_dir(text):
    with open(VAR_ROOT, 'w', encoding='utf-8' ) as f:
        if len(text) > 0:
            f.writelines('{0}'.format(text))
            print(OK + 'Корневой путь успешно добавлен' + RESET)
        else:
            print(ERROR + 'Ошибка! Поле не может быть пустым' + RESET)


#Добавляем файлы и папки для очистки
def add_directories(text):
    with open(VAR_ADD, 'a', encoding='utf-8') as f:
        if len(text) > 0:
            f.writelines('{0}\n'.format(text))
            print(OK + 'Файл или каталог успешно добавлен' + RESET)
            print_defis()
        else:
            print(ERROR + 'Ошибка! Поле не может быть пустым' + RESET)


#Функция удаления файлов и папок
def delet_file_dir():
    with open(VAR_ROOT, 'r', encoding='utf-8') as f:
        for root_dir_r in f:
            root_dir = root_dir_r.replace('\n', '')
    with open(VAR_ADD, 'r', encoding='utf-8') as f:
        for add_dir_r in f:
            add_dir = add_dir_r.replace('\n', '')
            result = os.path.join(root_dir, add_dir)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), result)
            if os.path.isfile(path):
                try:
                    os.unlink(path, dir_fd=None)
                    print('{}\n{}'.format(OK + 'Файл удален' + RESET, TEXT_COLOR_DIR + path + RESET))
                    print_defis()
                except OSError as e:
                    print('{}\n{}'.format(ERROR + 'Файла не существует' + RESET, TEXT_COLOR_DIR + path + RESET))
                    print_defis()
            else:
                try:
                    shutil.rmtree(path)
                    print('{}\n{}'.format(OK + 'Каталог удален' + RESET, TEXT_COLOR_DIR + path + RESET))
                    print_defis()
                except OSError as e:
                    print('{}\n{}'.format(ERROR + 'Каталог не требует очистки:' + RESET, TEXT_COLOR_DIR + path + RESET))
                    print_defis()
        print(OK + "Очистка каталогов и файлов прошла успешно!" + RESET)




if __name__ == '__main__':
    root_dir('test/test')
    add_directories('Ok')
    delet_file_dir()
