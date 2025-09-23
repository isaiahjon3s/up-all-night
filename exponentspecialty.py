import math

def main():
    x = float(input("Enter x value: "))
    xy = float(input("Enter xy value (x^y): "))
    
    result = exponentspecialty(x, xy)
    if result is not None:
        print(f"y = {result}")
        print(f"Verification: {x}^{result} = {x**result}")
    else:
        print("No solution found")

def exponentspecialty(x, xy):
    """
    Solve for y in the equation: xy = x^y
    Using numerical methods (Newton-Raphson method)
    """
    
    # Handle special cases
    if x <= 0:
        print("x must be positive")
        return None
    
    if xy <= 0:
        print("xy must be positive")
        return None
    
    if x == 1:
        if xy == 1:
            print("When x=1, any y works (1^y = 1 for any y)")
            return "any real number"
        else:
            print("No solution when x=1 and xy≠1")
            return None
    
    # For x^y = xy, we can take log of both sides:
    # log(xy) = y * log(x)
    # So y = log(xy) / log(x)
    
    try:
        y_simple = math.log(xy) / math.log(x)
        
        # Verify this solution works
        if abs(x**y_simple - xy) < 1e-10:
            return y_simple
        
        # If simple solution doesn't work, use Newton-Raphson method
        # We want to solve: f(y) = x^y - xy = 0
        # f'(y) = x^y * ln(x)
        
        def f(y):
            return x**y - xy
        
        def f_prime(y):
            return x**y * math.log(x)
        
        # Start with the simple solution as initial guess
        y = y_simple
        
        # Newton-Raphson iterations
        for i in range(100):  # Max 100 iterations
            try:
                fy = f(y)
                if abs(fy) < 1e-10:  # Close enough to zero
                    return y
                
                fy_prime = f_prime(y)
                if abs(fy_prime) < 1e-10:  # Avoid division by zero
                    break
                
                y_new = y - fy / fy_prime
                
                if abs(y_new - y) < 1e-10:  # Converged
                    return y_new
                
                y = y_new
                
            except (OverflowError, ValueError):
                break
        
        # If Newton-Raphson doesn't converge, try bisection method
        return solve_by_bisection(x, xy)
        
    except (ValueError, OverflowError):
        return solve_by_bisection(x, xy)

def solve_by_bisection(x, xy):
    """
    Solve x^y = xy using bisection method
    """
    def f(y):
        try:
            return x**y - xy
        except (OverflowError, ValueError):
            return float('inf') if y > 0 else float('-inf')
    
    # Find bounds where function changes sign
    y_low, y_high = -10, 10
    
    # Extend bounds if needed
    while f(y_low) * f(y_high) > 0 and y_high < 100:
        y_low -= 10
        y_high += 10
    
    if f(y_low) * f(y_high) > 0:
        return None  # No solution found in reasonable range
    
    # Bisection method
    for i in range(100):
        y_mid = (y_low + y_high) / 2
        f_mid = f(y_mid)
        
        if abs(f_mid) < 1e-10:
            return y_mid
        
        if f(y_low) * f_mid < 0:
            y_high = y_mid
        else:
            y_low = y_mid
        
        if abs(y_high - y_low) < 1e-10:
            return (y_low + y_high) / 2
    
    return None

if __name__ == "__main__":
    main()