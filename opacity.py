from color import is_valid_hex_color, hex_to_rgb, rgb_to_hex
from palette import get_color
from contrast import simple_contrast_handler, get_contrast_ratio
from termcolor import colored

"""
Blend two hex colors with the specified opacity level.
    
    Parameters:
    hex_color1 (str): The base hex color, starting with '#'.
    hex_color2 (str): The overlay hex color, starting with '#'.
    opacity (float): The opacity level of the second color (0.0 to 1.0).
    
    Returns:
    str: The resulting blended hex color.
"""
def blend_hex_colors(hex1, hex2, opacity_str):
		# Convert opacity from string to float in the range 0.0 to 1.0
    try:
        opacity = float(opacity_str)
    except ValueError:
        raise ValueError("Opacity must be a valid float string between 0.0 and 1.0")

    if not (0.0 <= opacity <= 1.0):
        print("Opacity must be between 0.0 and 1.0")
        return ""
    
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    
    blended_rgb = tuple(
        round((1 - opacity) * c1 + opacity * c2)
        for c1, c2 in zip(rgb1, rgb2)
    )
    
    return rgb_to_hex(blended_rgb)


def get_blended_color_contrast(hex_bottom, hex_middle, opacity, hex_top):
		blended_hex = blend_hex_colors(hex_bottom, hex_middle, opacity)
		if is_valid_hex_color(blended_hex):
				return get_contrast_ratio(blended_hex, hex_top)


"""
Calculates the color contrast with 
"""
def blended_color_contrast_handler(bottom, middle, opacity, top):
    hex_bottom = get_color(bottom)
    hex_middle = get_color(middle)
    hex_top = get_color(top)

    if not (
        is_valid_hex_color(hex_bottom)
        and is_valid_hex_color(hex_middle)
        and is_valid_hex_color(hex_top)
    ):
        print("Couldn't find contrast due to invalid colors.")
    else:
        blended_hex = blend_hex_colors(hex_bottom, hex_middle, opacity)
        if is_valid_hex_color(blended_hex):
            simple_contrast_handler(blended_hex, hex_top)

    return True

"""
Calculates the opacity of middle to meet the proper contrast ratio
with the top layer.
"""
def find_opacity_handler(bottom, middle, top):
		hex_bottom = get_color(bottom)
		hex_middle = get_color(middle)
		hex_top = get_color(top)

		if not (
        is_valid_hex_color(hex_bottom)
        and is_valid_hex_color(hex_middle)
        and is_valid_hex_color(hex_top)
    ):
				print("Couldn't find proper opacity due to invalid colors.")
		else:
				medium_contrast = None
				high_contrast = None

				contrast_with_bottom = get_contrast_ratio(hex_bottom, hex_top)
				contrast_with_middle = get_contrast_ratio(hex_middle, hex_top)

				# adding more of the middle layer makes the contrast worse
				if contrast_with_bottom > contrast_with_middle:
						opacity = 0.0

						while (medium_contrast == None or high_contrast == None) and opacity <= 1.0:
								contrast = get_blended_color_contrast(
                    hex_bottom, hex_middle, opacity, hex_top
								)
								if high_contrast == None and contrast < 4.5:
										high_contrast = opacity - 0.01
								if medium_contrast == None and contrast < 3.0:
										medium_contrast = opacity - 0.01
								opacity += 0.01

						if high_contrast == None:
								high_contrast = 1.0
						if medium_contrast == None:
								medium_contrast = 1.0
				# adding more of the middle layer makes the contrast better
				elif contrast_with_bottom < contrast_with_middle:
						opacity = 1.0

						while (medium_contrast == None or high_contrast == None) and opacity >= 0.0:
								contrast = get_blended_color_contrast(
                    hex_bottom, hex_middle, opacity, hex_top
								)
								if high_contrast == None and contrast < 4.5:
										high_contrast = opacity + 0.01
								if medium_contrast == None and contrast < 3.0:
										medium_contrast = opacity + 0.01
								opacity -= 0.01

						if high_contrast == None:
								high_contrast = 1.0
						if medium_contrast == None:
								medium_contrast = 1.0

				# print the results
				if high_contrast < 0 or high_contrast > 1.0:
						print("Couldn't find any 4.5 contrast")
				else:
						print(colored(f"{high_contrast:.2f}", "green"))

				if medium_contrast < 0 or medium_contrast > 1.0:
						print("Couldn't find any 3.0 contrast")
				else:
						print(colored(f"{medium_contrast:.2f}", "yellow"))

		return True
