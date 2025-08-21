def main():
    name = __name__
    reversed_name = reverse(name)
    print(reversed_name)

def reverse(name):
    return name[::-1]

if __name__ == "__main__":
    print("Testing reverse function...")
    test_name = "python"
    expected = "nohtyp"
    result = reverse(test_name)
    assert result == expected, f"Expected {expected}, but got {result}"
    print("All tests passed!")
    main()