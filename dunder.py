def print_dunders():
    print(__name__)
    print(__doc__)
    print(__file__)
    print(__package__)
    print(__cached__)
    print(__loader__)
    print(__spec__)
    print(__annotations__)
    print(__builtins__)
    print(__debug__)

if __name__ == "__main__":
    print_dunders()