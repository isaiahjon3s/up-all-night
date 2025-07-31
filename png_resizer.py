#!/usr/bin/env python3

import argparse
import sys
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Add padding around PNG images (white or transparent)")
    parser.add_argument("input", help="Input PNG file path")
    parser.add_argument("output", help="Output PNG file path")
    parser.add_argument("-p", "--padding", type=int, default=50, 
                       help="Uniform padding in pixels (default: 50)")
    parser.add_argument("-t", "--top", type=int, help="Top padding in pixels")
    parser.add_argument("-r", "--right", type=int, help="Right padding in pixels")
    parser.add_argument("-b", "--bottom", type=int, help="Bottom padding in pixels")
    parser.add_argument("-l", "--left", type=int, help="Left padding in pixels")
    parser.add_argument("-c", "--clear", action="store_true", 
                       help="Use transparent background instead of white")
    
    args = parser.parse_args()
    
    try:
        resize_png(args.input, args.output, args.padding, args.top, args.right, args.bottom, args.left, args.clear)
        print(f"Successfully resized {args.input} and saved to {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def resize_png(input_path, output_path, uniform_padding, top, right, bottom, left, use_transparent=False):
    """
    Resize a PNG image by adding padding around the edges.
    Uses white background by default, transparent if use_transparent is True.
    """
    # Open the input image
    try:
        img = Image.open(input_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{input_path}' not found")
    except Exception as e:
        raise Exception(f"Failed to open input file: {e}")
    
    # Convert to RGBA if not already (to handle transparency properly)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Determine padding values
    if any([top, right, bottom, left]):
        # Use individual padding values if any are specified
        top_pad = top if top is not None else 0
        right_pad = right if right is not None else 0
        bottom_pad = bottom if bottom is not None else 0
        left_pad = left if left is not None else 0
    else:
        # Use uniform padding
        top_pad = right_pad = bottom_pad = left_pad = uniform_padding
    
    # Calculate new dimensions
    original_width, original_height = img.size
    new_width = original_width + left_pad + right_pad
    new_height = original_height + top_pad + bottom_pad
    
    # Create new image with background (white or transparent)
    if use_transparent:
        # Transparent background
        background_color = (0, 0, 0, 0)  # Fully transparent
    else:
        # White background
        background_color = (255, 255, 255, 255)  # Opaque white
    
    new_img = Image.new('RGBA', (new_width, new_height), background_color)
    
    # Paste the original image onto the new image
    paste_x = left_pad
    paste_y = top_pad
    new_img.paste(img, (paste_x, paste_y), img if img.mode == 'RGBA' else None)
    
    # Convert back to RGB if the original was RGB and we're not using transparency
    if img.mode == 'RGB' and not use_transparent:
        new_img = new_img.convert('RGB')
    
    # Save the result
    try:
        new_img.save(output_path, 'PNG')
    except Exception as e:
        raise Exception(f"Failed to save output file: {e}")

if __name__ == "__main__":
    main()