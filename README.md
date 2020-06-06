# CleaningOfGarbage
Script to delete directories.

Настройка программы:

1. Способ и самый простой:
	A. Создайте файл way.txt используя ваш любимый редактор. Добавьте корневой путь к каталогам
		Пример: /data/data/com.termux/files/home/storage/shared
	B. Создайте файл dir_del.txt используя ваш любимый редактор. Добавьте директории или файлы которые вы хотите удалять. Каждая директория или файл должны указываться с новой строки.

2. Способ:
	A. Запустите скрипт python main.py с командой way а после укажите полный путь к корневому каталогу
		Пример: python main.py way /data/data/com.termux/files/home/storage/shared
		Скрипт автоматически создаст файл way.txt и запишет в него строку
	B. Запустите скрипт python main.py с командой dir а после укажите каталог или файл который вы хотите удалять. 
		Пример: python main.py dir folder
	Скрипт создаст файл dir_del.txt и будет записать в него все файлы и папки для удаления с новой строки без перезаписи.
	C. Для удаления файлов или каталогов по заданным настройкам используйте команду del запустив скрипт соответствующим образом python main.py del 
	Не переживайте если вы увидите ошибку "каталог или файл не найден" это означает лишь то что ваша система его ещё не создала, данная ошибка не приведет к остановке сценария удаления

-------------------------------------------------------------

Setting up program:
1. The method and simplest:
	A. Create a way.txt file using your favorite editor.
Add root directory path
		Example: /data/data/com.termux/files/home/storage/shared
	B. Create a file dir_del.txt using your favorite editor. Add the directories or files you want to delete. Each directory or file must be specified from a new line.

2. Way:
	A. Run the python main.py script with the way command and then specify the full path to the root directory
		Example: python main.py way /data/data/com.termux/files/home/storage/shared
	The script will automatically create a way.txt file and write a string to it
	B. Run the python main.py script with the dir command and then specify the directory or file you want to delete.
Example: python main.py dir folder. The script will create a dir_del.txt file and write all files and folders to it for deletion from the new line without overwriting.
	C. To delete files or directories according to the specified settings, use the del command by running the script accordingly python main.py del
	Do not worry if you see the error "directory or file not found" it only means that your system has not created it yet, this error will not stop the deletion script
