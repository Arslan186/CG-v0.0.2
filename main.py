import os, sys, shutil
from setting import WAY, LIST_OF_DIRECTORIES

#Функция перебора директорий по указанному пути
def write_in_f():
    f = open('nameFolder.txt', 'w')
    way_dir = WAY['name_dir']
    list_way = os.listdir(way_dir) #Перебираем директории;
    for name_sort in list_way:
        if f.write(f'{name_sort}\n'):
            print(name_sort)
            print_t()
        else:
            print("error")

def delete_dir():
    f = open('nameFolder.txt', 'r')
    result_f = f.readlines()
    print(result_f)
    print_t()
    f = open('del_folder.txt', 'r')
    result_d = f.readlines()
    print(result_d)
    print_t()
    sort = [x for x in result_f if x in result_d]
    print(sort)
    print_t()

    #way_dir = WAY['name_dir']
    #for way_dir + sort:
    #path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'TestDir')
    #shutil.rmtree(path)
    




def print_t():
    print("-" * 50)
write_in_f()
delete_dir()


#f = open('del_folder.txt', 'r')
 #           list_d = f.readlines()
  #          print(list_d)
            #Res = [x for x in name_sort if x in list_d]
            #print(Res)
