driving_age = {
    "usa": 16,
    "uk": 17,
    "canada": 16,
    "australia": 16,
    "new zealand": 16,
    "ireland": 17,
    "south africa": 16,
    "india": 18,
}


def main():
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age")
        return
    country = input("Enter your country: ").lower()
    if country not in driving_age:
        print("Invalid country")
        print("Valid countries are: ", ", ".join(driving_age.keys()))
        return
    if age >= driving_age[country]:
        print("You are old enough to drive")
    else:
        print("You are not old enough to drive")


if __name__ == "__main__":
    main()