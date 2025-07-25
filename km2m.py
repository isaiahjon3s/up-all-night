def main():
    km = float(input("Enter a distance in kilometers: "))
    print(f"{km} kilometers is {get_miles(km)} miles")

def get_miles(km):
    return km * 0.621371

if __name__ == "__main__":
    main()