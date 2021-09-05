from variable import *


def print_defis():
    print('{:^10s}'.format(DEFIS_COLOR + DEFIS + RESET))


def option_ok():
    print(OK + 'Выполнено' + RESET)
    print_defis()
