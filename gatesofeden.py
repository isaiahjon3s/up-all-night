def main():
    password = input("Set Password: ")

    length = len(password)
    space = ''
    while True:
        for _ in range(length -1):
            print(f'#'*length + f'{space}     {space}' + '#'*length, end='\n')
        print(f'#'*length + f'{space}  $  {space}' + '#'*length, end='\n')
        guess = input("Guess: ")
        if guess == password:
            break
        else:
            length += 1
            space = space + ' '
    for j in range(length):
        print(f'#'*length*2)



if __name__ == "__main__":
    main()