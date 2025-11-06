from datetime import *

def main():
    if datetime.now().hour < 12:
        print("Good morning!")
    elif datetime.now().hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")

if __name__ == "__main__":
    main()