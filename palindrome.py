def main():
    word = (input("Enter word: "))
    print(palindrome(word))

def palindrome(word):
    word = word.lower()
    word = list(word)
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

if __name__ == "__main__":
    main()