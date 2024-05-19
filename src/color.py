import re

"""
Checks if the string "str" is a valid hex color.
"""


def is_valid_hex_color(str):
    hex_color_pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    return bool(re.match(hex_color_pattern, str))


"""
Converts a hex value to an RGB value and returns it as a tuple.
For example, #FAFAFA -> (250, 250, 250)
"""


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    rgb = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return rgb


"""
Converts an RGB value to a hex value and returns it as a string.
For example, (250, 250, 250) -> #FAFAFA
"""


def rgb_to_hex(rgb_color):
    return "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])
