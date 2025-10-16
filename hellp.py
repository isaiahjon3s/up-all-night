def main():
    text = input("Enter a text: ")
    print(hellp(text))

def hellp(text):
    hellped = ""
    for i, (current, next) in enumerate(zip(text, text[1:])): # text[1:] is the rest of the text
        if current == "l" and next != "l":
            hellped += "ll"
        else:
            hellped += current
    # Add the last character (it doesn't get zipped)
    if text:
        hellped += text[-1]
    return hellped

if __name__ == "__main__":
    main()
        
