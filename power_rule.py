import re

def main():
    get_input = input("Enter a function: ")
    print(power_rule(get_input))

def power_rule(func):
    # Match forms like 3x^2, x^5, 7x^3, etc.
    match = re.fullmatch(r"\s*(\d*)x\^(\d+)\s*", func)
    if match:
        a = match.group(1)
        n = int(match.group(2))
        a = int(a) if a else 1
        new_coeff = a * n
        new_exp = n - 1
        if new_exp == 1:
            return f"{new_coeff}x"
        elif new_exp == 0:
            return f"{new_coeff}"
        else:
            return f"{new_coeff}x^{new_exp}"
    else:
        return "Invalid function. Please enter in the form ax^n (e.g., 3x^2, x^5)"
    
if __name__ == "__main__":
    main()