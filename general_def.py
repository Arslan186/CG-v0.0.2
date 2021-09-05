from variable import *
import os

def print_defis():
    print('{:^10s}'.format(DEFIS_COLOR + DEFIS + RESET))


def option_ok():
    print(OK + 'Выполнено' + RESET)
    print_defis()

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
