import random, sys

def main():
    whatyawant()

def whatyawant():
    kill = random.randint(1, 100000)
    guesses = 0
    while True:
        print("This is what you want") # This is what you want
        print("This is what you get") # This is what you get
        guess = random.randint(1, 100000)
        if guess == kill:
            sys.exit(f"You get it in {guesses} guesses")
        else:
            guesses += 1

if __name__ == "__main__":
    main()