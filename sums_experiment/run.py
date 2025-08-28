from sums import get_data
import json

# CONFIGURATION
SIZE_OF_DATA = 50  # Range of numbers to analyze (0 to SIZE_OF_DATA-1) = 1  # The number to track percentage for

def main(target_number: int):
    result = {}
    
    for i in range(SIZE_OF_DATA):
        data = get_data(i)
        
        if data:  # If there are combinations for this number
            target_count = data.get(target_number, 0)
            total_count = sum(data.values())
            percentage = round((target_count / total_count) * 100, 2) if total_count > 0 else 0
        else:
            percentage = 0
        
        result[str(i)] = percentage
    
    # Save to JSON file
    output_file = f"data_{target_number}_percentages.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
