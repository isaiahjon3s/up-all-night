# Create an empty ascii picture frame of custom size
import argparse

def main():
    parser = argparse.ArgumentParser(description="ASCIIPicture Frame Generator")
    parser.add_argument("-p", "--padding", type=int, help="size of picture frame in addition to standard size")

    args = parser.parse_args()

    padding = args.padding

    if padding == None:
        padding = 0
    
    print(get_picture_frame(padding))
    
def get_picture_frame(padding):
    dimentions = 5 + padding

    frame = ""

    frame += "-" * (dimentions + 2) # top border
    frame += "\n"

    for _ in range(dimentions): # middle sides
        frame += "|" + " " * (dimentions) + "|\n"

    frame += "-" * (dimentions + 2) # bottom border
    frame += "\n"
    return frame
if __name__ == "__main__":
    main()