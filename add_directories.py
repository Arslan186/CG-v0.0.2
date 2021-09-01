from variable import *
#Добавляем файлы и папки для очистки
def add_directories(text):
    with open('/data/data/com.termux/files/home/storage/shared/CG-v0.0.2/add_dir.txt', 'a', encoding='utf-8') as f:
        if len(text) > 0:
            f.writelines('{0}\n'.format(text))
            print(OK + 'Файл или каталог успешно добавлен' + RESET)
        else:
            print(ERROR + 'Ошибка! Поле не может быть пустым' + RESET)


if __name__ == '__main__':
    add_directories('Ok')
