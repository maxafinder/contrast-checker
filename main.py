import os

palette = {}
bg, fg, text = [], [], []  # [name, hex]


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

"""
Returns the hex value of a color given a color name from the palette.
If a hex value is given for name, then it is returned.
For example, "gray-900" -> "#18181B"
"""


def parse_color(name):
    if name[0] == "#":
        return name

    color, level_value = name.split("-")
    levels = palette[color]
    for level in levels:
        if level[0] == level_value:
            return level[1]
    return ""


"""
Replaces fg, bg, and text with the default values.
If default overrides exist in "defaults.txt", then those are used.
"""


def set_defaults():
    global bg
    global fg
    global text
    bg, fg, text = ["", "#FFFFFF"], ["", "#000000"], ["", "#000000"]

    f = open("defaults.txt", "r")
    lines = f.readlines()

    for line in lines:
        prop, name = line.split(", ")
        name = name.strip()
        hex = parse_color(name)
        if prop == "bg":
            bg = [name, hex]
        elif prop == "fg":
            fg = [name, hex]
        else:
            text = [name, hex]


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


def invalid_command(command):
    print(
        'Command "'
        + command
        + '" not found.\nEnter "help" to see a list of valid commands.'
    )


def print_prop_handler(prop):
    # bg
    if prop == "bg" and bg[0] == "":
        print(bg[1])
    elif prop == "bg":
        print(bg[0] + ", " + bg[1])
    # fg
    elif prop == "fg" and fg[0] == "":
        print(fg[1])
    elif prop == "fg":
        print(fg[0] + ", " + fg[1])
    # text
    elif prop == "text" and text[0] == "":
        print(text[1])
    elif prop == "text":
        print(text[0] + ", " + text[1])
    else:
        return False
    return True


#def set_prop_handler(prop, value):

    

def command_handler(command):
    if command == "clear":
        os.system("clear")
        return

    tokens = command.split(" ")
    if len(tokens) == 0:
        invalid_command(command)
        return

    if tokens[0] == "p" and len(tokens) == 2:
        res = print_prop_handler(tokens[1])
        if not res:
            invalid_command(command)
    elif tokens[1] == 's' and len(tokens) == 3:
        res = set_prop_handler(tokens[1], tokens[2])
    else:
        invalid_command(command)


def main():
    palette = parse_color_palette()
    set_defaults()

    while True:
        command = input("> ")
        if command == "exit":
            break
        command_handler(command)

if __name__ == "__main__":
    main()
