def main():
    input_str = input("Enter a string: ")
    if parenthesis_check(input_str):
        print("The string is valid")
    else:
        print("The string is invalid")

def parenthesis_check(input_str):
    options = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for char in input_str:
        if char in options: # if the character is an opening parenthesis, add it to the stack
            stack.append(char)
        elif char in options.values(): # if the character is a closing parenthesis, check if the stack is empty or if the top of the stack is the corresponding opening parenthesis
            if not stack or options[stack.pop()] != char: # if the stack is empty or the top of the stack is not the corresponding opening parenthesis, return False
                return False
    return len(stack) == 0 # if the stack is empty, return True, otherwise return False

if __name__ == "__main__":
    main()