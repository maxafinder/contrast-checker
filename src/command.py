import os
from src.properties import print_prop_handler, set_prop_handler, swap_props_handler
from src.contrast import simple_contrast_handler, color_contrast_handler, all_contrast_handler
from src.opacity import blended_color_contrast_handler, find_opacity_handler, find_opacity_at_level_handler, find_opacity_between_levels_handler, blend_colors_handler


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
        if len(tokens) == 5 and tokens[2] == "-l":
            res = find_opacity_at_level_handler(tokens[1], tokens[3], tokens[4])
        elif len(tokens) == 5:
            res = blended_color_contrast_handler(tokens[1], tokens[2], tokens[3], tokens[4])
        elif len(tokens) == 4:
            res = find_opacity_handler(tokens[1], tokens[2], tokens[3])
        elif len(tokens) == 6:
            res = find_opacity_between_levels_handler(tokens[1], tokens[3], tokens[5])
    elif tokens[0] == "b" and len(tokens) == 4:
        res = blend_colors_handler(tokens[1], tokens[2], tokens[3])

    if not res:
        invalid_command(command)
