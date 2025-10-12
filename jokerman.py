import random
def main():
    text = input("Enter a text: ")
    print(jokerman(text))

def jokerman(text):
    emojis = ["🤡", "🤠", "🤢", "🤮","👹","👺","👻","👽","🤖","👿"]
    for letter in text:
        text = text.replace(letter, random.choice(emojis))
    return text

if __name__ == "__main__":
    main()