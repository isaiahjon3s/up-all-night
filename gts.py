import random

def gts():
    yn = random.choice(["y", "n"])
    if yn == "y":
        print("Go to sleep")
    else:
        print("Stay up")

if __name__ == "__main__":
    gts()