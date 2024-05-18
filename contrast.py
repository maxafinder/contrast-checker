from properties import bg, fg, text
from color import hex_to_rgb
from palette import palette, get_color
from termcolor import colored


def relative_luminance(rgb):
    """Calculate the relative luminance of an RGB color."""

    def channel_luminance(channel):
        c = channel / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return (
        0.2126 * channel_luminance(r)
        + 0.7152 * channel_luminance(g)
        + 0.0722 * channel_luminance(b)
    )


def get_contrast_ratio(hex1, hex2):
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)

    lum1 = relative_luminance(rgb1)
    lum2 = relative_luminance(rgb2)

    if lum1 > lum2:
        ratio = (lum1 + 0.05) / (lum2 + 0.05)
    else:
        ratio = (lum2 + 0.05) / (lum1 + 0.05)

    return round(ratio, 2)


def print_contrast_ratio(contrast):
    if contrast < 3.0:
        print(colored(f"{contrast:.2f}".ljust(5), "red"), end="")
    elif contrast < 4.5:
        print(colored(f"{contrast:.2f}".ljust(5), "yellow"), end="")
    else:
        print(colored(f"{contrast:.2f}".ljust(5), "green"), end="")


def simple_contrast_handler(val1, val2):
    hex1 = get_color(val1)
    hex2 = get_color(val2)

    if hex1 != "" and hex2 != "":
        contrast = get_contrast_ratio(hex1, hex2)
        print_contrast_ratio(contrast)
        print()
    else:
        print("Could not get contrast ratio due to invalid colors.")

    return True


def color_contrast_handler(val, color):
    hex = get_color(val)
    if hex == "":
        print("Could not get contrast ratio due to invalid colors.")
        return

    if color in palette:
        print(color.ljust(12), end="")
        levels = palette[color]
        for level in levels:
            contrast = get_contrast_ratio(hex, level[1])
            print("(" + level[0] + ") ", end="")
            print_contrast_ratio(contrast)
            print("   ", end="")
        print()

    return True


def all_contrast_handler(val):
		hex = get_color(val)
		if hex == "":
				print("Could not get contrast ratio due to invalid colors.")
				return

		for color in palette.keys():
				color_contrast_handler(hex, color)
				print()
        
		return True
