from palette import palette, get_color
from color import is_valid_hex_color


bg, fg, text = [], [], []  # [name, hex]

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
				hex = get_color(name)

				if hex == "":
						print('Unable to find color: "' + name + '"')
						return
				if is_valid_hex_color(name):
						name = ""
	
				if prop == "bg":
						bg = [name, hex]
				elif prop == "fg":
						fg = [name, hex]
				else:
						text = [name, hex]


def hex_from_prop(prop):
		hex = ""
		if prop == "bg":
				hex = bg[1]
		elif prop == "fg":
				hex = fg[1]
		elif prop == "text":
				hex = text[1]
		return hex


"""
Prints the value of a property.
prop -> the property we are setting (bg/fg/text).
"""


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
		elif get_color(prop) != "":
				print(get_color(prop))
		else:
				return False
		return True


"""
Sets the value of a property.
prop -> the property we are setting (bg/fg/text).
name -> the variable name or hex value of the color.
"""


def set_prop_handler(prop, name):
    global bg
    global fg
    global text

    # bg
    if prop == "bg" and is_valid_hex_color(name):
        bg[0] = ""
        bg[1] = name
    elif prop == "bg":
        res = get_color(name)
        if is_valid_hex_color(res):
            bg[0] = name
            bg[1] = res
        else:
            print(res)
    # fg
    elif prop == "fg" and is_valid_hex_color(name):
        fg[0] = ""
        fg[1] = name
    elif prop == "fg":
        res = get_color(name)
        if is_valid_hex_color(res):
            fg[0] = name
            fg[1] = res
        else:
            print(res)
    # text
    elif prop == "text" and is_valid_hex_color(name):
        text[0] = ""
        text[1] = name
    elif prop == "text":
        res = get_color(name)
        if is_valid_hex_color(res):
            text[0] = name
            text[1] = res
        else:
            print(res)
    else:
        return False
    return True


"""
Swap the values of two properties
prop1 -> the property (bg/fg/text) we are swapping with "prop2". 
prop2 -> the property (bg/fg/text) we are swapping with "prop1". 
"""


def swap_props_handler(prop1, prop2):
    global bg
    global fg
    global text
    if (prop1 == "bg" and prop2 == "fg") or (prop1 == "fg" and prop2 == "bg"):
        temp = bg
        bg = fg
        fg = temp
    elif (prop1 == "bg" and prop2 == "text") or (prop1 == "text" and prop2 == "bg"):
        temp = bg
        bg = text 
        text = temp
    elif (prop1 == "fg" and prop2 == "text") or (prop1 == "text" and prop2 == "fg"):
        temp = fg 
        fg = text
        text = temp
    else:
        return False
    return True
