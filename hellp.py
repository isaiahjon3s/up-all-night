import random

def main():
    text = input("Enter a text: ")
    print(hellp(text))

def hellp(text):
    hellped = ""
    i = 0
    while i < len(text):
        if text[i] == "l" and not (text[i+1] == "l" or text[i-1] == "l"):
            hellped += "ll"
        else:
            hellped += text[i]
        i += 1
    return hellped

if __name__ == "__main__":
    main()
        
