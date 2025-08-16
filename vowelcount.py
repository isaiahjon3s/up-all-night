

def main():
    string = input("Enter a string: ")
    print(vowel_count(string))


def vowel_count(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count


if __name__ == "__main__":
    main()