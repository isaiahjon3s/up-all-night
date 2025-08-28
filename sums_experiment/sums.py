def main():
    num = int(input("Number: "))
    print(get_data(num))

def get_data(num: int) -> list:
    return analyze(sums(num))


def sums(n: int) -> list: # Return all possible combinations of numbers that sum to n where all numbers are greater than 1
    if n < 2:
        return []
    
    result = []
    
    def find_combinations(target, current_combination, start):
        if target == 0:
            result.append(current_combination[:])
            return
        
        for i in range(start, target + 1):
            if i >= 2:  # All numbers must be greater than 1
                current_combination.append(i)
                find_combinations(target - i, current_combination, i)
                current_combination.pop()
    
    find_combinations(n, [], 2)
    return result

def analyze(combinations: list) -> dict: # Analyze the combinations and return a dictionary with the analysis
    top_nums = {}
    for combination in combinations:
        for num in combination:
            if num not in top_nums:
                top_nums[num] = 1
            else:
                top_nums[num] += 1
    return top_nums

if __name__ == "__main__":
    main()
