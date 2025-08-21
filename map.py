def main():
    text = input("Text to use map function in python: ")
    print(map_text(text))

def upper(text):
    return text.upper()
    
def map_text(text):
    return "".join(map(upper, text))

if __name__ == "__main__":
    main()