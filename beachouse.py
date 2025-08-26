def main():
    text = input("Sentence: ")
    print(beachouse(text))\

def beachouse(s: str) -> str: # Returns string with any double letters (word end letter same as next word start letter) removed
    housed = ""
    i = 0
    while i < len(s):
        letter = s[i]
        if letter == " " and i > 0 and i < len(s) - 1:
            if s[i-1] == s[i+1]:  # previous char equals next char
                housed += s[i+1]  # add the next character
                i += 2  # skip the next character since we already added it
            else:
                housed += letter
                i += 1
        else:
            housed += letter
            i += 1
    return housed



if __name__ == "__main__":
    main()