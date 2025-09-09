import sys
fruits = {
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape"
    "honeydew",
    "kiwi"
}

def main():
    fruit = input("Enter a fruit: ").lower().strip()
    if fruit == "fiona":
        print("APPLE!")
        sys.exit()
    elif fruit == "apple":
        print("FIONA!")
        sys.exit()
    if fruit in fruits:
        print(f"{fruit} is a fruit")
    else:
        print(f"{fruit} is not a fruit")

if __name__ == "__main__":
    main()
