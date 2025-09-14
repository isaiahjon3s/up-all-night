bad_words = [
    "kill",
    "shoot", 
    "shit",
    "fuck",
    "ass",
    "bitch",
    "cunt",
    "dick",
    "pussy",
    "cock",
    "vagina",
    "penis",
    "anus",
    "tits",
    "boobs",
    "porn",
    "sex"
]
def main():
    text = input("Enter a text: ")
    print(redact(text))

def redact(text):
    bad_count = 0
    for word in text.split():
        if word in bad_words:
            text = text.replace(word, "*" * len(word))
            bad_count += 1
    if bad_count == 0:
        return "No bad words found!"
    return text

if __name__ == "__main__":
    main()