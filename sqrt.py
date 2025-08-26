def main():
    number = int(input("Enter a number: "))
    print(sqrt(number))

def sqrt(number):
    sqrts = []
    for i in range(1, number):
        square = i * i
        if square == number:
            return square
        if square <= number:
            sqrts.append(i)
        else:
            return sqrts[-1]
    

if __name__ == "__main__":
    main()