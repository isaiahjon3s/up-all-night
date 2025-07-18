import sys


def main():
    num = input("Number: ")
    if num.isdigit():
        print(complicator(num))
    else:
        sys.exit("Not a number 🥀")

def complicator(num):
    num = int(num)
    complicant = ("1 + ") * num + "1"
    return complicant

if __name__ == "__main__":
    main()

