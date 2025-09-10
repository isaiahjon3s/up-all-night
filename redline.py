import random

def main():
    str = input("Enter a string: ")
    location = input("Enter a location for the redline: ")
    print(redline(str, location))

redlines = [
    "❗️",
    "📍", 
    "🚨",
    "❌",
    "🚫",
    "🔴",
    "📌",
    "♦️"
]
def insert(text, position, char_to_insert):
    """Insert a character at a specific position in a string"""
    if position < 0:
        position = 0
    elif position > len(text):
        position = len(text)
    return text[:position] + char_to_insert + text[position:]

def redline(str:str, location:int):
    redline_char = random.choice(redlines)
    str = str.strip()
    location = int(location)
    redlined = insert(str, location, redline_char)
    return redlined

if __name__ == "__main__":
    main()
