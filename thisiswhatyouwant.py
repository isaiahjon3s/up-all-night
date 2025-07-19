import random, sys

ODDS = 100000000
def main():
    whatyawant()

def whatyawant():
    kill = random.randint(1, ODDS)
    guesses = 0
    while True:
        print("This is what you want") # This is what you want
        print("This is what you get") # This is what you get
        guess = random.randint(1, ODDS)
        if guess == kill:
            sys.exit(f"You get it in {guesses} guesses")
        else:
            guesses += 1

if __name__ == "__main__":
    main()