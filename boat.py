import random

def main():
    if random.randint(0, 1) == 0:
        print("The boat is going to sink")
    else:
        print("The boat is going to float")

if __name__ == "__main__":
    main()