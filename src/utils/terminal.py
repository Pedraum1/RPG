import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def set_color_white():
    return "\033[30m"

def set_color_red():
    return "\033[31m"

def set_color_yellow():
    return "\033[33m"

def set_color_green():
    return "\033[32m"

def set_color_blue():
    return "\033[34m"

def print_square():
    return "\u25A0"

def print_empty_square():
    return "\u25A1"