import math
import argparse
from typing import Optional, Dict, Tuple
from dataclasses import dataclass

@dataclass
class UnitSystem:
    """Define unit systems for kinematic calculations."""
    name: str
    velocity: str
    acceleration: str
    time: str
    distance: str

# Define common unit systems
UNIT_SYSTEMS = {
    'metric': UnitSystem('Metric (SI)', 'm/s', 'm/s²', 's', 'm'),
    'imperial': UnitSystem('Imperial', 'ft/s', 'ft/s²', 's', 'ft'),
    'automotive': UnitSystem('Automotive', 'mph', 'mph/s', 's', 'ft'),
    'physics': UnitSystem('Physics', 'm/s', 'm/s²', 's', 'm')
}

def main():
    parser = argparse.ArgumentParser(
        description="Kinematic equations calculator with unit support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Unit Systems:
  metric     - m/s, m/s², s, m (default)
  imperial   - ft/s, ft/s², s, ft  
  automotive - mph, mph/s, s, ft
  physics    - m/s, m/s², s, m (same as metric)

Examples:
  python kinematics.py --v0 10 --vf 20 --a 2 --t 5 --units metric
  python kinematics.py --v0 30 --a 9.8 --t 3 --d 100 --units imperial
        """
    )
    
    parser.add_argument("--v0", type=float, help="Initial velocity")
    parser.add_argument("--vf", type=float, help="Final velocity") 
    parser.add_argument("--a", type=float, help="Acceleration")
    parser.add_argument("--t", type=float, help="Time")
    parser.add_argument("--d", type=float, help="Distance (change)")
    parser.add_argument("--units", choices=list(UNIT_SYSTEMS.keys()), 
                       default='metric', help="Unit system to use (default: metric)")
    
    args = parser.parse_args()
    
    # Check that exactly 4 values are provided (we solve for the 5th)
    values = [args.v0, args.vf, args.a, args.t, args.d]
    provided_count = sum(1 for v in values if v is not None)
    
    if provided_count != 4:
        print(f"Error: Please provide exactly 4 values (provided {provided_count})")
        print(f"Using unit system: {UNIT_SYSTEMS[args.units].name}")
        return
    
    unit_system = UNIT_SYSTEMS[args.units]
    result = kinematic_solver(args.v0, args.vf, args.a, args.t, args.d, unit_system)
    print(result)

def format_results(v0: float, vf: float, a: float, t: float, d: float, 
                  unit_system: UnitSystem) -> str:
    """Format the kinematic equation results with appropriate units."""
    variables = [
        ('v0', v0, unit_system.velocity),
        ('vf', vf, unit_system.velocity),
        ('a', a, unit_system.acceleration),
        ('t', t, unit_system.time),
        ('d', d, unit_system.distance)
    ]
    
    # Format each value with units, handling None values gracefully
    formatted_parts = []
    for name, value, unit in variables:
        if value is not None:
            formatted_parts.append(f"{name} = {value:.3f} {unit}")
    
    result = ", ".join(formatted_parts)
    return f"Results ({unit_system.name}): {result}"

def kinematic_solver(v0: Optional[float], vf: Optional[float], a: Optional[float], 
                    t: Optional[float], d: Optional[float], unit_system: UnitSystem) -> str:
    """
    Solve kinematic equations given 4 of 5 variables.
    Uses the standard kinematic equations:
    1. vf = v0 + at
    2. d = v0*t + 0.5*a*t²
    3. vf² = v0² + 2ad
    
    Args:
        v0: Initial velocity
        vf: Final velocity
        a: Acceleration
        t: Time
        d: Distance (displacement)
        unit_system: UnitSystem object defining the units to use
    
    Returns:
        Formatted string with results and units
    """
    
    try:
        # Determine which variable to solve for
        if v0 is None:
            # Solve for v0 using: v0 = vf - at
            if vf is not None and a is not None and t is not None:
                v0 = vf - a * t
            else:
                # Use alternative equation: vf² = v0² + 2ad -> v0 = sqrt(vf² - 2ad)
                v0 = math.sqrt(vf**2 - 2*a*d)
                
        elif vf is None:
            # Solve for vf using: vf = v0 + at
            if v0 is not None and a is not None and t is not None:
                vf = v0 + a * t
            else:
                # Use alternative equation: vf² = v0² + 2ad
                vf = math.sqrt(v0**2 + 2*a*d)
                
        elif a is None:
            # Solve for a using: a = (vf - v0) / t
            if v0 is not None and vf is not None and t is not None:
                a = (vf - v0) / t
            else:
                # Use alternative equation: vf² = v0² + 2ad -> a = (vf² - v0²) / (2d)
                a = (vf**2 - v0**2) / (2*d)
                
        elif t is None:
            # Solve for t using: t = (vf - v0) / a
            if v0 is not None and vf is not None and a is not None:
                t = (vf - v0) / a
            else:
                # Use quadratic formula from d = v0*t + 0.5*a*t²
                # 0.5*a*t² + v0*t - d = 0
                discriminant = v0**2 + 2*a*d
                if discriminant < 0:
                    return "Error: No real solution for time"
                t = (-v0 + math.sqrt(discriminant)) / a
                
        elif d is None:
            # Solve for d using: d = v0*t + 0.5*a*t²
            d = v0 * t + 0.5 * a * t**2
            
        return format_results(v0, vf, a, t, d, unit_system)
        
    except (ZeroDivisionError, ValueError, TypeError) as e:
        return f"Error in calculation: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    main()