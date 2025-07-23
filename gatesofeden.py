def main():
    password = input("Set Password: ")

    length = len(password)
    while True:
        for i in range(length -1):
            print(f'#'*length + '}     {' + '#'*length, end='\n')
        print(f'#'*length + '}  $  {' + '#'*length, end='\n')
        guess = input("Guess: ")
        if guess == password:
            break
        else:
            length += 1
    for j in range(length):
        print(f'#'*length*2)



if __name__ == "__main__":
    main()