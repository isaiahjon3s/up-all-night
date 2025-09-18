import struct
import math

def main():
    """Test the fast inverse square root algorithm with various inputs."""
    print("=== Fast Inverse Square Root Algorithm (Quake III) ===\n")
    
    test_values = [1.0, 4.0, 9.0, 16.0, 25.0, 0.5, 2.5, 100.0]
    
    print("Testing against standard library math.sqrt():")
    print("Value\t\tFast InvSqrt\tMath InvSqrt\tError")
    print("-" * 55)
    
    for val in test_values:
        fast_result = fast_inverse_sqrt(val)
        math_result = 1.0 / math.sqrt(val)
        error = abs(fast_result - math_result)
        
        print(f"{val:8.1f}\t{fast_result:12.8f}\t{math_result:12.8f}\t{error:.2e}")
    
    print("\n" + "="*60)
    print("Detailed step-by-step example with x = 4.0:")
    print("="*60)
    
    # Demonstrate one calculation with verbose output
    example_val = 4.0
    print(f"\nCalculating 1/√{example_val} = {1.0/math.sqrt(example_val):.8f}")
    print("Step-by-step breakdown:")
    fast_result = fast_inverse_sqrt(example_val)
    
    print(f"\nFinal result: {fast_result:.8f}")
    print(f"Correct answer: {1.0/math.sqrt(example_val):.8f}")
    print(f"Error: {abs(fast_result - 1.0/math.sqrt(example_val)):.2e}")
    print(f"Accuracy: {(1 - abs(fast_result - 1.0/math.sqrt(example_val))/(1.0/math.sqrt(example_val))) * 100:.4f}%")

def fast_inverse_sqrt(x):
    """
    The legendary fast inverse square root algorithm from Quake III Arena.
    
    This algorithm computes 1/√x approximately 4x faster than the standard method
    by using clever bit manipulation and IEEE 754 floating point representation.
    
    Args:
        x (float): Input value (should be positive)
    
    Returns:
        float: Approximation of 1/√x
    """
    
    # Step 1: Convert float to 32-bit integer representation
    # This treats the IEEE 754 bits as an integer without changing the bits
    threehalfs = 1.5
    x2 = x * 0.5
    
    # Pack the float as bytes, then unpack as unsigned int
    # This is the modern Python equivalent of the C union trick
    packed_y = struct.pack('f', x)
    i = struct.unpack('I', packed_y)[0]
    
    print(f"  Step 1 - Original float: {x}")
    print(f"  Step 1 - As 32-bit int:  0x{i:08x} ({i})")
    
    # Step 2: The magic number!
    # 0x5f3759df is carefully chosen based on IEEE 754 format analysis
    # This gives us a good initial approximation
    i = 0x5f3759df - (i >> 1)
    
    print(f"  Step 2 - After magic:    0x{i:08x} ({i})")
    print(f"  Step 2 - Magic constant: 0x5f3759df")
    print(f"  Step 2 - Bit shift >>1:  Divides exponent by 2")
    
    # Step 3: Convert back to float
    # This gives us our initial approximation
    packed_i = struct.pack('I', i)
    y = struct.unpack('f', packed_i)[0]
    
    print(f"  Step 3 - Initial approx: {y:.8f}")
    
    # Step 4: Newton-Raphson iteration for refinement
    # This dramatically improves accuracy with just one iteration
    # Formula: y = y * (1.5 - (x/2) * y * y)
    y = y * (threehalfs - (x2 * y * y))
    
    print(f"  Step 4 - After Newton:   {y:.8f}")
    print(f"  Step 4 - Newton formula: y = y * (1.5 - (x/2) * y²)")
    
    # Optional: Second iteration for even better accuracy
    # y = y * (threehalfs - (x2 * y * y))
    
    return y

def fast_inverse_sqrt_silent(x):
    """
    Fast inverse square root without debug output - for actual use.
    
    Args:
        x (float): Input value (should be positive)
    
    Returns:
        float: Approximation of 1/√x
    """
    threehalfs = 1.5
    x2 = x * 0.5
    
    # Step 1: Reinterpret float bits as integer
    packed_y = struct.pack('f', x)
    i = struct.unpack('I', packed_y)[0]
    
    # Step 2: Magic number and bit manipulation
    i = 0x5f3759df - (i >> 1)
    
    # Step 3: Convert back to float
    packed_i = struct.pack('I', i)
    y = struct.unpack('f', packed_i)[0]
    
    # Step 4: Newton-Raphson refinement
    y = y * (threehalfs - (x2 * y * y))
    
    return y

def explain_algorithm():
    """
    Detailed explanation of how the fast inverse square root works.
    """
    
    print("\n" + "="*70)
    print("HOW THE FAST INVERSE SQUARE ROOT ALGORITHM WORKS")
    print("="*70)
    
    print("""
🎯 GOAL: Compute 1/√x quickly and accurately

🧠 THE GENIUS INSIGHT:
The algorithm exploits the IEEE 754 floating-point representation:
- Float = Sign bit + 8 Exponent bits + 23 Mantissa bits
- We can treat these bits as an integer for mathematical operations!

📊 STEP-BY-STEP BREAKDOWN:

1️⃣  REINTERPRET BITS
   • Take the float's raw bits and treat them as a 32-bit integer
   • This doesn't change the bits, just how we interpret them
   • Example: 4.0 = 0x40800000 as bits

2️⃣  THE MAGIC NUMBER: 0x5f3759df
   • This number was derived through mathematical analysis
   • It's based on the IEEE 754 format and logarithm properties
   • When we do: magic - (input >> 1), we get close to 1/√x
   • The >> 1 shift effectively halves the exponent

3️⃣  BIT MANIPULATION MATH
   • For IEEE 754: log₂(number) ≈ (bits_as_int - bias) / 2²³
   • We want log₂(1/√x) = -½ × log₂(x)
   • The magic constant gives us the right offset

4️⃣  NEWTON-RAPHSON REFINEMENT
   • The bit trick gives a good approximation (~5% error)
   • One iteration of Newton's method: y = y(1.5 - xy²/2)
   • This reduces error to ~0.2%!

⚡ WHY IT'S FAST:
   • No division operations
   • No expensive sqrt() calls
   • Just bit shifts, multiplication, and subtraction
   • ~4x faster than standard sqrt() in the 1990s

🎮 HISTORICAL CONTEXT:
   • Found in Quake III Arena source code (1999)
   • Used for lighting calculations and 3D graphics
   • Attributed to John Carmack, but likely has earlier origins
   • Became famous when Quake source was released

🔬 THE MATHEMATICS:
   The magic constant comes from:
   • IEEE 754 exponent bias (127)
   • Mantissa scaling (2²³)
   • Mathematical relationship: R = (3/2)×2²³×(127 - μ)
   • Where μ ≈ 0.0450466 is an empirically optimized constant
    """)

if __name__ == "__main__":
    explain_algorithm()
    main()