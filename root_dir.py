from variable import *

#Добавить корневой путь для очистки
def root_dir(text):
    with open('/data/data/com.termux/files/home/storage/shared/CG-v0.0.2/root_dir.txt', 'w', encoding='utf-8' ) as f:
        if len(text) > 0:
            f.writelines('{0}'.format(text))
            print(OK + 'Корневой путь успешно добавлен' + RESET)
        else:
            print(ERROR + 'Ошибка! Поле не может быть пустым' + RESET)


if __name__ == '__main__':
    root_dir('/data/data/com.termux/files/home/storage/shared/')
