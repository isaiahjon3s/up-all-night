def main():
    word = input("Enter a word: ")
    print(improv(word.strip().replace(" ", "")))

alphabet = list("abcdefghijklmnopqrstuvwxyza")

def improv(word):
    if not word[0].isalpha():
        return "Invalid word"
    last_letter = word[-1]
    next_letter = ""
    i = 0
    while i < 28:
        if alphabet[i] == last_letter:
            next_letter += alphabet[i+1]
            break
        i += 1
    improvd = f"{word}{next_letter}"
    return improvd


    

if __name__ == "__main__":
    main()