from src.palette import palette, parse_color_palette
from src.properties import set_defaults
from src.command import command_handler

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
