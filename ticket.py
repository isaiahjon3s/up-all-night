import random, sys, argparse

def main():
    parser = argparse.ArgumentParser(description="Ticket generator")
    parser.add_argument("-g", "--password prompt", type=str, help="Creates password from prompt and will return a ticket")
    args = parser.parse_args()
    
    if args.generate:
        print(generate_ticket(args.generate))

def generate_ticket(str):
    input = list(str)
    pw = ""
    for i in range(len(input) - 1):
        pw += input[i]
        i += 2
    return f"{pw}.pw"

if __name__ == "__main__":
    main()