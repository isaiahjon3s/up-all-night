def main():
    input_text = input("Enter a number or word to see if it's a palindrome: ")
    if palindrome(input_text):
        print("Palindrome")
    else:
        print("Not a palindrome")

# Saw this on leetcode and it was so beautiful I had to save it here <3
def palindrome(n):
        return str(n) == str(n)[::-1]
    
if __name__ == "__main__":
    main()