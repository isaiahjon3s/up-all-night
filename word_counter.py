def main():
    text = input("Text: ")
    print(count(text))

def count(text):
    words = text.split(" ")
    return len(words)

if __name__ == "__main__":
    main()