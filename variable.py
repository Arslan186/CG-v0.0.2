from colored import fg, bg, attr
#Variable COLOR
ERROR = bg(196)
OK = bg(26) + fg(52)
DEFIS_COLOR = fg(88)
TEXT_COLOR = fg(0)
TEXT_COLOR_INPUT = bg(34) + fg(0)
TEXT_COLOR_DIR = bg(240) + fg(0)
RESET = attr(0)

#Variable GENERAL
DEFIS = '--------------------------------------------------------'

MENU_OPTIONS = {
        1: 'Укажите корневой каталог',
        2: 'Укажите файлы и папки для очистки',
        3: 'Очистить',
        4: 'Выход',
        }


VAR_ROOT = 'root_dir.txt'
VAR_ADD = 'add_dir.txt'
