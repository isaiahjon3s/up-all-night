#!/usr/bin/env python3
"""
Demonstration script for the Terminal Graphing Calculator
"""

import subprocess
import time
import sys

def run_demo():
    """Run a series of demonstrations of the graphing calculator."""
    
    demos = [
        {
            "title": "Quadratic Function: x²",
            "command": ["python", "terminalgrapher.py", "x^2"],
            "description": "A simple parabola"
        },
        {
            "title": "Sine Wave: sin(x)",
            "command": ["python", "terminalgrapher.py", "sin(x)", "--xmin", "-6.28", "--xmax", "6.28", "--ymin", "-2", "--ymax", "2"],
            "description": "A sine wave over two periods"
        },
        {
            "title": "Cubic Function: x³ - 3x",
            "command": ["python", "terminalgrapher.py", "x^3 - 3*x", "--xmin", "-3", "--xmax", "3", "--ymin", "-10", "--ymax", "10"],
            "description": "A cubic function with local extrema"
        },
        {
            "title": "Logarithmic Function: log(x)",
            "command": ["python", "terminalgrapher.py", "log(x)", "--xmin", "0.1", "--xmax", "10", "--ymin", "-3", "--ymax", "3"],
            "description": "Natural logarithm function"
        },
        {
            "title": "Square Root: √x",
            "command": ["python", "terminalgrapher.py", "sqrt(x)", "--xmin", "0", "--xmax", "16", "--ymin", "0", "--ymax", "4"],
            "description": "Square root function"
        },
        {
            "title": "Cosine with Grid: cos(x)",
            "command": ["python", "terminalgrapher.py", "cos(x)", "--xmin", "-6.28", "--xmax", "6.28", "--ymin", "-2", "--ymax", "2", "--grid"],
            "description": "Cosine wave with grid lines for better visualization"
        },
        {
            "title": "Exponential: e^x",
            "command": ["python", "terminalgrapher.py", "exp(x)", "--xmin", "-3", "--xmax", "3", "--ymin", "0", "--ymax", "20"],
            "description": "Exponential function"
        },
        {
            "title": "Complex Function: x² + sin(x)",
            "command": ["python", "terminalgrapher.py", "x^2 + sin(x)", "--xmin", "-4", "--xmax", "4", "--ymin", "-5", "--ymax", "20"],
            "description": "Combination of polynomial and trigonometric functions"
        }
    ]
    
    print("=" * 80)
    print("TERMINAL GRAPHING CALCULATOR DEMONSTRATION")
    print("=" * 80)
    print()
    
    for i, demo in enumerate(demos, 1):
        print(f"Demo {i}: {demo['title']}")
        print(f"Description: {demo['description']}")
        print("-" * 80)
        
        try:
            result = subprocess.run(demo['command'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(f"Error: {result.stderr}")
        except subprocess.TimeoutExpired:
            print("Demo timed out")
        except Exception as e:
            print(f"Error running demo: {e}")
        
        print("\n" + "=" * 80)
        
        if i < len(demos):
            input("Press Enter to continue to the next demo...")
            print()
    
    print("\nInteractive Mode Demo:")
    print("You can also run the calculator in interactive mode:")
    print("python terminalgrapher.py --interactive")
    print("\nThis allows you to:")
    print("- Enter expressions dynamically")
    print("- Zoom in/out with 'zoom xmin xmax ymin ymax'")
    print("- Toggle grid with 'grid on/off'")
    print("- Reset view with 'reset'")
    print("- Type 'quit' to exit")

if __name__ == "__main__":
    run_demo()
