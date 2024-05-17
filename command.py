import os
from properties import print_prop_handler, set_prop_handler, swap_props_handler
from contrast import simple_contrast_handler


def invalid_command(command):
    print(
        'Command "'
        + command
        + '" not found.\nEnter "help" to see a list of valid commands.'
    )


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
		elif tokens[0] == "c" and len(tokens) == 3:
				res = simple_contrast_handler(tokens[1], tokens[2])
        
		if not res:
				invalid_command(command)
