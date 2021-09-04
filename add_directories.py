from variable import *
from general_def import *


#Добавляем файлы и папки для очистки
def add_directories(text):
    with open(VAR_ADD, 'a', encoding='utf-8') as f:
        if len(text) > 0:
            f.writelines('{0}\n'.format(text))
            print(OK + 'Файл или каталог успешно добавлен' + RESET)
            print_defis()
        else:
            print(ERROR + 'Ошибка! Поле не может быть пустым' + RESET)


if __name__ == '__main__':
    add_directories('Ok')
