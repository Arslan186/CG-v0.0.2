import os
import os.path
import shutil


#Добавить путь для удаления папок
def write_way(text):
    with open('way.txt', 'a', encoding='utf-8' ) as f:
        try:
            f.writelines('{0}\n'.format(text))
        except TypeError:
            print('Необходимо указать путь к корневому каталогу.\nПо умолчанию на андроид устройствах следующий путь:\n/data/data/com.termux/files/home/storage/shared')


#Добавить дириктррии для удаления
def write_dir_del_folder(text):
    with open('dir_del.txt', 'a', encoding='utf-8') as f:
        try:
            f.writelines('{0}\n'.format(text))
        except TypeError:
            print('Необходимо указать каталог или файл')

#Склеить пути дирикторий
def delet():
    with open('way.txt', 'r', encoding='utf-8') as f:
        for line_w in f:
            result_w = line_w
    with open('dir_del.txt', 'r', encoding='utf-8') as f:
        for line_d in f:
            result_d = line_d.replace('\n', '')
            result_dir = os.path.join(result_w, result_d)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), result_dir)
            if os.path.isfile(path):
                try:
                    os.unlink(path, dir_fd=None)
                    print(path, "Ok")
                except OSError as e:
                    print("Ошибка: %s : %s" % (path, e.strerror))
            else:
                try:
                    shutil.rmtree(path)
                    print(path, "Ok")
                except OSError as e:
                    print("Ошибка: %s : %s" % (path, e.strerror))
        print("Очистка каталогов и файлов прошла успешно!")


if __name__ == '__main__':
    write_dir_del_folder('test1\n' 'test2\n' 'test3\n')
    write_way('set/set')
    delet()
