import os
import os.path
import shutil


#Добавить путь для удаления папок
def write_way(text=None):
    with open('way.txt', 'w', encoding='utf-8' ) as f:
        if text:
            f.write(text)


#Добавить дириктррии для удаления
def write_dir_del_folder(text=None):
    with open('dir_del.txt', 'w', encoding='utf-8') as f:
        if text:
            f.writelines(text)


#Склеить пути и дирикторий
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
    #write_dir_del_folder('test1\n' 'test2\n' 'test3\n')
    #write_way('/storage/shared/')
    delet()
