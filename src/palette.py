from src.color import is_valid_hex_color

palette = {}

"""
Parses the colors into a dictionary where each color maps to an array of tupes.
Each tuple contains the level value and the hex value of the color.
"""


def parse_color_palette():
    f = open("palette.txt", "r")
    lines = f.readlines()

    while len(lines) > 0:
        color = lines[0].strip()
        lines = lines[1:]
        palette[color] = []

        while len(lines) > 0:
            if lines[0] == "\n":
                lines = lines[1:]
                break
            level_value, hex = lines[0].split(", ")
            palette[color] += [(level_value.strip(), hex.strip())]
            lines = lines[1:]

    return palette


"""
Returns the hex value of a color given a color name from the palette.
If a hex value is given for name, then it is returned.
For example, "gray-900" -> "#18181B"
"""


def get_color(name):
    from src.properties import hex_from_prop

    if is_valid_hex_color(name):
        return name

    res = hex_from_prop(name)
    if res != "":
        return res

    color, level_value = name.split("-")
    if color in palette:
        levels = palette[color]
        for level in levels:
            if level[0] == level_value:
                return level[1]

    return ""
