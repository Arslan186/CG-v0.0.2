import os
import os.path
import shutil
from variable import *
from root_dir import *
from add_directories import *


#Функция удаления файлов и папок
def delet_file_dir():
    with open('root_dir.txt', 'r', encoding='utf-8') as f:
        for root_dir_r in f:
            root_dir = root_dir_r.replace('\n', '')
    with open('add_dir.txt', 'r', encoding='utf-8') as f:
        for add_dir_r in f:
            add_dir = add_dir_r.replace('\n', '')
            result = os.path.join(root_dir, add_dir)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), result)
            if os.path.isfile(path):
                try:
                    os.unlink(path, dir_fd=None)
                    print('{}\n{}'.format(OK + 'Файл удален' + RESET, path))
                    print(DEFIS)
                except OSError as e:
                    print('{}\n{}'.format(ERROR + 'Файла не существует' + RESET, path))
                    print(DEFIS)
            else:
                try:
                    shutil.rmtree(path)
                    print('{}\n{}'.format(OK + 'Каталог удален' + RESET, path))
                    print(DEFIS)
                except OSError as e:
                    print('{}\n{}'.format(ERROR + 'Каталог не требует очистки:' + RESET, path))
                    print(DEFIS)
        print(OK + "Очистка каталогов и файлов прошла успешно!" + RESET)


if __name__ == '__main__':
    delet_file_dir()
