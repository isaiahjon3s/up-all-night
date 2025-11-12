from argparse import *

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "orange": (255, 165, 0),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42),
    "gray": (128, 128, 128),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "lime": (128, 255, 0),
    "maroon": (128, 0, 0),
    "navy": (0, 0, 128),
    "olive": (128, 128, 0),
    "purple": (128, 0, 128),
}

def main():
    parser = ArgumentParser(description="LED Color Desired")
    parser.add_argument("-c", "--color", type=str, help="Color to calculate")
    args = parser.parse_args()

    if args.color is None or args.color.lower().strip() not in colors:
        print("Error: Color not found")
        return
    else:
        print(f"The color {args.color.lower().strip()} is {colors[args.color.lower().strip()]}")

if __name__ == "__main__":
    main()