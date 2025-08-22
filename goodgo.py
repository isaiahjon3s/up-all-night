def main():
    word = input("Enter a word: ")
    goodgoed = goodgo(word)
    print(goodgoed)

def goodgo(word):
    goodgoed = ""
    for i in range(len(word)):
        if i % 2 == 0:
            goodgoed += word[i]
        else:
            goodgoed += word[i].upper()
    return goodgoed

if __name__ == "__main__":
    main()