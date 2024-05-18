import os
from properties import print_prop_handler, set_prop_handler, swap_props_handler
from contrast import simple_contrast_handler, color_contrast_handler, all_contrast_handler
from opacity import blended_color_contrast_handler, find_opacity_handler


def invalid_command(command):
    print('Command "' + command + '" not found.')


def command_handler(command):
    if command == "clear":
        os.system("clear")
        return

    tokens = command.split(" ")
    if len(tokens) == 0:
        invalid_command(command)
        return

    # property commands
    res = False
    if tokens[0] == "p" and len(tokens) == 2:
        res = print_prop_handler(tokens[1])
    elif tokens[0] == "s" and len(tokens) == 3:
        res = set_prop_handler(tokens[1], tokens[2])
    elif tokens[0] == "swap" and len(tokens) == 3:
        res = swap_props_handler(tokens[1], tokens[2])
    # contrast commands
    elif tokens[0] == "c":
        if len(tokens) == 3:
            res = simple_contrast_handler(tokens[1], tokens[2])
        elif len(tokens) == 4 and tokens[2] == "-c":
            res = color_contrast_handler(tokens[1], tokens[3])
        elif len(tokens) == 2:
            res = all_contrast_handler(tokens[1])
    # opacity commands
    elif tokens[0] == "o":
        if len(tokens) == 5:
            res = blended_color_contrast_handler(tokens[1], tokens[2], tokens[3], tokens[4])
        elif len(tokens) == 4:
            res = find_opacity_handler(tokens[1], tokens[2], tokens[3])

    if not res:
        invalid_command(command)
