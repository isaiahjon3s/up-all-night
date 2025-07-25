def walrus():
    if (user_input := input("Possible walrus: ").lower()) == "walrus":
        print("Walrus")
    else:
        print("Not a walrus")

if __name__ == "__main__":
    walrus()