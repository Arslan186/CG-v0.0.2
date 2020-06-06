import sys
from core import write_dir_del_folder, write_way, delet

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду --help')
else:
    if command == 'way':
        try:
            text = sys.argv[2]
        except:
            print('Укажите вторым аргументом путь к корневому каталогу')
        else:
            write_way(text)
    elif command == 'dir':
        try:
            text = sys.argv[2]
        except:
            print('Укажите вторым аргументом имя каталога или файла')
        else:
            write_dir_del_folder(text)
    elif command == 'del':
        delet()
    elif command == '--help':
        print('way укажите корневой путь к каталогам')
        print('dir укажите папки и файлы для удаления')
        print('del команда очистки')
