# Terminal Graphing Calculator

A powerful command-line graphing calculator that plots mathematical functions directly in the terminal using ASCII characters.

## Features

- **Mathematical Function Support**: Supports a wide range of mathematical functions including trigonometric, logarithmic, exponential, and polynomial functions
- **Interactive Mode**: Real-time graphing with zoom, pan, and grid controls
- **Customizable Viewport**: Adjustable domain and range for detailed analysis
- **Grid Visualization**: Optional grid lines for better coordinate reference
- **High Resolution**: Smooth curve plotting using line interpolation
- **Multiple Plot Styles**: Different characters for different functions

## Supported Functions

### Basic Operations
- `+`, `-`, `*`, `/` - Arithmetic operations
- `^` or `**` - Exponentiation
- `()` - Parentheses for grouping

### Mathematical Functions
- `sin(x)`, `cos(x)`, `tan(x)` - Trigonometric functions
- `asin(x)`, `acos(x)`, `atan(x)` - Inverse trigonometric functions
- `sinh(x)`, `cosh(x)`, `tanh(x)` - Hyperbolic functions
- `log(x)` - Natural logarithm
- `log10(x)` - Base-10 logarithm
- `sqrt(x)` - Square root
- `abs(x)` - Absolute value
- `exp(x)` - Exponential function (e^x)

### Constants
- `pi` - π (3.14159...)
- `e` - Euler's number (2.71828...)

## Usage

### Command Line Mode

```bash
# Basic usage
python terminalgrapher.py "x^2"

# With custom domain and range
python terminalgrapher.py "sin(x)" --xmin -6.28 --xmax 6.28 --ymin -2 --ymax 2

# With grid lines
python terminalgrapher.py "cos(x)" --grid

# Custom terminal size
python terminalgrapher.py "x^3" --width 100 --height 30
```

### Interactive Mode

```bash
python terminalgrapher.py --interactive
```

In interactive mode, you can:
- Enter mathematical expressions to graph
- Use commands:
  - `zoom xmin xmax ymin ymax` - Zoom to specific coordinates
  - `grid on/off` - Toggle grid lines
  - `reset` - Reset to default view
  - `quit` - Exit the program

## Examples

### Quadratic Function
```bash
python terminalgrapher.py "x^2"
```

### Sine Wave
```bash
python terminalgrapher.py "sin(x)" --xmin -6.28 --xmax 6.28 --ymin -2 --ymax 2
```

### Complex Function
```bash
python terminalgrapher.py "x^2 + sin(x)" --xmin -4 --xmax 4 --ymin -5 --ymax 20
```

### Logarithmic Function
```bash
python terminalgrapher.py "log(x)" --xmin 0.1 --xmax 10 --ymin -3 --ymax 3
```

## Command Line Options

- `expression` - Mathematical expression to graph
- `--width WIDTH` - Terminal width (default: 80)
- `--height HEIGHT` - Terminal height (default: 24)
- `--xmin XMIN` - Minimum x value (default: -10)
- `--xmax XMAX` - Maximum x value (default: 10)
- `--ymin YMIN` - Minimum y value (default: -10)
- `--ymax YMAX` - Maximum y value (default: 10)
- `--grid` - Show grid lines
- `--interactive` - Enter interactive mode

## Technical Details

The calculator uses:
- **Bresenham's Line Algorithm** for smooth curve plotting
- **Safe Expression Evaluation** for security
- **Coordinate System Mapping** for accurate scaling
- **ASCII Art Rendering** for terminal display

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Demo

Run the demonstration script to see various examples:

```bash
python demo_grapher.py
```

This will show a series of different mathematical functions and their visualizations.

## Tips

1. **For smooth curves**: Use higher resolution by increasing the terminal width
2. **For detailed analysis**: Use the zoom feature in interactive mode
3. **For better visualization**: Enable grid lines with `--grid`
4. **For complex functions**: Use parentheses to ensure proper order of operations
5. **For trigonometric functions**: Use appropriate domain ranges (e.g., -2π to 2π for sine/cosine)

## Limitations

- Terminal display is limited by character resolution
- Very steep functions may appear discontinuous
- Some functions may have domain restrictions (e.g., log(x) for x ≤ 0)
- Complex numbers are not supported

## License

This project is open source and available under the MIT License.
