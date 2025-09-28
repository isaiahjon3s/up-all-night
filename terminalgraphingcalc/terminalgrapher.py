#!/usr/bin/env python3
"""
Terminal Graphing Calculator
A command-line graphing calculator that can plot mathematical functions in the terminal.
"""

import math
import re
import sys
from typing import List, Tuple, Optional, Callable
import argparse


class TerminalGrapher:
    def __init__(self, width: int = 80, height: int = 24):
        self.width = width
        self.height = height
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        
    def set_domain(self, x_min: float, x_max: float):
        """Set the x-axis domain for plotting."""
        self.x_min = x_min
        self.x_max = x_max
        
    def set_range(self, y_min: float, y_max: float):
        """Set the y-axis range for plotting."""
        self.y_min = y_min
        self.y_max = y_max
        
    def clear_grid(self):
        """Clear the plotting grid."""
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
    def world_to_screen(self, x: float, y: float) -> Tuple[int, int]:
        """Convert world coordinates to screen coordinates."""
        screen_x = int((x - self.x_min) / (self.x_max - self.x_min) * (self.width - 1))
        screen_y = int((self.y_max - y) / (self.y_max - self.y_min) * (self.height - 1))
        return screen_x, screen_y
        
    def screen_to_world(self, screen_x: int, screen_y: int) -> Tuple[float, float]:
        """Convert screen coordinates to world coordinates."""
        x = self.x_min + (screen_x / (self.width - 1)) * (self.x_max - self.x_min)
        y = self.y_max - (screen_y / (self.height - 1)) * (self.y_max - self.y_min)
        return x, y
        
    def plot_point(self, x: float, y: float, char: str = '*'):
        """Plot a single point on the grid."""
        if self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max:
            screen_x, screen_y = self.world_to_screen(x, y)
            if 0 <= screen_x < self.width and 0 <= screen_y < self.height:
                self.grid[screen_y][screen_x] = char
                
    def plot_line(self, x1: float, y1: float, x2: float, y2: float, char: str = '*'):
        """Plot a line between two points using Bresenham's algorithm."""
        screen_x1, screen_y1 = self.world_to_screen(x1, y1)
        screen_x2, screen_y2 = self.world_to_screen(x2, y2)
        
        # Bresenham's line algorithm
        dx = abs(screen_x2 - screen_x1)
        dy = abs(screen_y2 - screen_y1)
        sx = 1 if screen_x1 < screen_x2 else -1
        sy = 1 if screen_y1 < screen_y2 else -1
        err = dx - dy
        
        x, y = screen_x1, screen_y1
        
        while True:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = char
                
            if x == screen_x2 and y == screen_y2:
                break
                
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
                
    def draw_axes(self):
        """Draw the x and y axes."""
        # Draw x-axis
        if self.y_min <= 0 <= self.y_max:
            x_start, y_start = self.world_to_screen(self.x_min, 0)
            x_end, y_end = self.world_to_screen(self.x_max, 0)
            for x in range(max(0, x_start), min(self.width, x_end + 1)):
                if 0 <= y_start < self.height:
                    self.grid[y_start][x] = '-'
                    
        # Draw y-axis
        if self.x_min <= 0 <= self.x_max:
            x_start, y_start = self.world_to_screen(0, self.y_min)
            x_end, y_end = self.world_to_screen(0, self.y_max)
            for y in range(max(0, y_start), min(self.height, y_end + 1)):
                if 0 <= x_start < self.width:
                    self.grid[y][x_start] = '|'
                    
        # Draw origin
        if self.x_min <= 0 <= self.x_max and self.y_min <= 0 <= self.y_max:
            origin_x, origin_y = self.world_to_screen(0, 0)
            if 0 <= origin_x < self.width and 0 <= origin_y < self.height:
                self.grid[origin_y][origin_x] = '+'
                
    def draw_grid_lines(self):
        """Draw grid lines for better visualization."""
        # Vertical grid lines
        for i in range(int(self.x_min), int(self.x_max) + 1):
            if i != 0:  # Don't draw on the y-axis
                x_start, y_start = self.world_to_screen(i, self.y_min)
                x_end, y_end = self.world_to_screen(i, self.y_max)
                for y in range(max(0, y_start), min(self.height, y_end + 1)):
                    if 0 <= x_start < self.width:
                        if self.grid[y][x_start] == ' ':
                            self.grid[y][x_start] = '.'
                            
        # Horizontal grid lines
        for i in range(int(self.y_min), int(self.y_max) + 1):
            if i != 0:  # Don't draw on the x-axis
                x_start, y_start = self.world_to_screen(self.x_min, i)
                x_end, y_end = self.world_to_screen(self.x_max, i)
                for x in range(max(0, x_start), min(self.width, x_end + 1)):
                    if 0 <= y_start < self.height:
                        if self.grid[y_start][x] == ' ':
                            self.grid[y_start][x] = '.'
                            
    def add_labels(self):
        """Add axis labels and tick marks."""
        # X-axis labels
        if self.y_min <= 0 <= self.y_max:
            origin_x, origin_y = self.world_to_screen(0, 0)
            for i in range(int(self.x_min), int(self.x_max) + 1):
                if i != 0:
                    x_pos, y_pos = self.world_to_screen(i, 0)
                    if 0 <= x_pos < self.width and 0 <= y_pos < self.height:
                        # Add tick mark
                        if y_pos + 1 < self.height:
                            self.grid[y_pos + 1][x_pos] = '|'
                        # Add label (simplified)
                        if abs(i) < 10:  # Only show single digit labels
                            label = str(i)
                            for j, char in enumerate(label):
                                if x_pos + j < self.width and y_pos + 2 < self.height:
                                    self.grid[y_pos + 2][x_pos + j] = char
                                    
        # Y-axis labels
        if self.x_min <= 0 <= self.x_max:
            origin_x, origin_y = self.world_to_screen(0, 0)
            for i in range(int(self.y_min), int(self.y_max) + 1):
                if i != 0:
                    x_pos, y_pos = self.world_to_screen(0, i)
                    if 0 <= x_pos < self.width and 0 <= y_pos < self.height:
                        # Add tick mark
                        if x_pos + 1 < self.width:
                            self.grid[y_pos][x_pos + 1] = '-'
                        # Add label (simplified)
                        if abs(i) < 10:  # Only show single digit labels
                            label = str(i)
                            for j, char in enumerate(label):
                                if x_pos + 2 + j < self.width and y_pos < self.height:
                                    self.grid[y_pos][x_pos + 2 + j] = char
                                    
    def plot_function(self, func: Callable[[float], float], char: str = '*', resolution: int = None):
        """Plot a mathematical function."""
        if resolution is None:
            resolution = self.width * 2  # Higher resolution for smoother curves
            
        prev_x = None
        prev_y = None
        
        for i in range(resolution + 1):
            x = self.x_min + (i / resolution) * (self.x_max - self.x_min)
            try:
                y = func(x)
                if math.isfinite(y):  # Check for NaN or infinity
                    if prev_x is not None and prev_y is not None:
                        # Draw line segment for smooth curves
                        self.plot_line(prev_x, prev_y, x, y, char)
                    else:
                        # First point
                        self.plot_point(x, y, char)
                    prev_x, prev_y = x, y
                else:
                    prev_x, prev_y = None, None
            except (ValueError, ZeroDivisionError, OverflowError):
                prev_x, prev_y = None, None
                
    def render(self):
        """Render the grid to the terminal."""
        print("\n" + "=" * self.width)
        for row in self.grid:
            print(''.join(row))
        print("=" * self.width)
        print(f"Domain: [{self.x_min:.2f}, {self.x_max:.2f}]")
        print(f"Range: [{self.y_min:.2f}, {self.y_max:.2f}]")


class FunctionParser:
    """Parse mathematical expressions and convert them to callable functions."""
    
    def __init__(self):
        self.functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'log10': math.log10,
            'sqrt': math.sqrt,
            'abs': abs,
            'exp': math.exp,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
        }
        
    def parse(self, expression: str) -> Callable[[float], float]:
        """Parse a mathematical expression and return a callable function."""
        # Handle powers (^ to **)
        expression = expression.replace('^', '**')
        
        # Handle implicit multiplication (e.g., 2x -> 2*x)
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expression)
        expression = re.sub(r'\)(\d)', r')*\1', expression)
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        
        # Create a safe evaluation environment
        safe_dict = {
            '__builtins__': {},
            'x': 0,  # Placeholder
            'pi': math.pi,
            'e': math.e,
        }
        safe_dict.update(self.functions)
        
        try:
            # Compile the expression
            code = compile(expression, '<string>', 'eval')
            
            def func(x):
                safe_dict['x'] = x
                return eval(code, {"__builtins__": {}}, safe_dict)
                
            return func
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}. Error: {e}")


def main():
    parser = argparse.ArgumentParser(description='Terminal Graphing Calculator')
    parser.add_argument('expression', nargs='?', help='Mathematical expression to graph (e.g., "x^2", "sin(x)", "x^2 + 2*x + 1")')
    parser.add_argument('--width', type=int, default=80, help='Terminal width (default: 80)')
    parser.add_argument('--height', type=int, default=24, help='Terminal height (default: 24)')
    parser.add_argument('--xmin', type=float, default=-10, help='Minimum x value (default: -10)')
    parser.add_argument('--xmax', type=float, default=10, help='Maximum x value (default: 10)')
    parser.add_argument('--ymin', type=float, default=-10, help='Minimum y value (default: -10)')
    parser.add_argument('--ymax', type=float, default=10, help='Maximum y value (default: 10)')
    parser.add_argument('--grid', action='store_true', help='Show grid lines')
    parser.add_argument('--interactive', action='store_true', help='Interactive mode')
    
    args = parser.parse_args()
    
    # Create grapher
    grapher = TerminalGrapher(args.width, args.height)
    grapher.set_domain(args.xmin, args.xmax)
    grapher.set_range(args.ymin, args.ymax)
    
    if args.interactive:
        # Interactive mode
        parser_obj = FunctionParser()
        print("Terminal Graphing Calculator - Interactive Mode")
        print("Enter mathematical expressions to graph (type 'quit' to exit)")
        print("Examples: x^2, sin(x), x^2 + 2*x + 1, log(x), sqrt(x)")
        print("Commands: 'zoom xmin xmax ymin ymax', 'reset', 'grid on/off'")
        
        show_grid = False
        
        while True:
            try:
                user_input = input("\nEnter expression or command: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                elif user_input.lower() == 'reset':
                    grapher.set_domain(-10, 10)
                    grapher.set_range(-10, 10)
                    show_grid = False
                    print("Reset to default view")
                    continue
                elif user_input.lower() == 'grid on':
                    show_grid = True
                    print("Grid enabled")
                    continue
                elif user_input.lower() == 'grid off':
                    show_grid = False
                    print("Grid disabled")
                    continue
                elif user_input.startswith('zoom '):
                    try:
                        parts = user_input.split()
                        if len(parts) == 5:
                            xmin, xmax, ymin, ymax = map(float, parts[1:])
                            grapher.set_domain(xmin, xmax)
                            grapher.set_range(ymin, ymax)
                            print(f"Zoomed to x:[{xmin}, {xmax}], y:[{ymin}, {ymax}]")
                        else:
                            print("Usage: zoom xmin xmax ymin ymax")
                    except ValueError:
                        print("Invalid zoom values")
                    continue
                
                # Parse and plot the function
                func = parser_obj.parse(user_input)
                grapher.clear_grid()
                
                if show_grid:
                    grapher.draw_grid_lines()
                grapher.draw_axes()
                grapher.add_labels()
                grapher.plot_function(func, '*')
                grapher.render()
                
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
                
    elif args.expression:
        # Single expression mode
        try:
            parser_obj = FunctionParser()
            func = parser_obj.parse(args.expression)
            
            grapher.clear_grid()
            if args.grid:
                grapher.draw_grid_lines()
            grapher.draw_axes()
            grapher.add_labels()
            grapher.plot_function(func, '*')
            grapher.render()
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # Show help and examples
        print("Terminal Graphing Calculator")
        print("\nUsage examples:")
        print("  python terminalgrapher.py 'x^2'")
        print("  python terminalgrapher.py 'sin(x)' --xmin -2*pi --xmax 2*pi")
        print("  python terminalgrapher.py 'x^2 + 2*x + 1' --grid")
        print("  python terminalgrapher.py --interactive")
        print("\nSupported functions: sin, cos, tan, log, log10, sqrt, abs, exp, asin, acos, atan, sinh, cosh, tanh")
        print("Constants: pi, e")
        print("Operators: +, -, *, /, ** (power), ^ (power)")


if __name__ == "__main__":
    main()
