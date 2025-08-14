def main():
    while True:
        try:
            input_num = int(input("Enter a number: "))
            if input_num > 1:
                break
        except ValueError:
            continue
    if isprime(input_num):
        print(f"{input_num} is a prime number")
    else:
        print(f"{input_num} is not a prime number")

def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()