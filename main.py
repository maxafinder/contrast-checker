def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    rgb = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return rgb


def rgb_to_hex(rgb_color):
    return "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])


def get_defaults():
    f = open("defaults.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)

"""
Parses the colors into a dictionary where each color maps to an array of tupes.
Each tuple contains the level value and the hex value of the color.
"""
def parse_color_palette():
    f = open("palette.txt", "r")
    lines = f.readlines()

    palette = {}

    while len(lines) > 0:
        color = lines[0]
        lines = lines[1:]
        palette[color] = []

        while len(lines) > 0:
            if lines[0] == "\n":
                lines = lines[1:]
                break
            name, value = lines[0].split(", ")
            palette[color] += [(name.strip(), value.strip())]
            lines = lines[1:]

    for color in palette.keys():
        print(color)
        for level in palette[color]:
            value, hex = level 
            print(value)
            print(hex)
        print()

    return palette


def main():
    palette = parse_color_palette()
    # get_defaults()


if __name__ == "__main__":
    main()
