#!/usr/bin/env python3
"""
Generate premium placeholder images for Portergeist Art portfolio
Dark gradients with category labels and accent borders
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Portfolio images data
portfolio_images = [
    {'filename': 'portfolio-1.jpg', 'category': 'Neo-Traditional', 'gradient': ('#1a0000', '#8B0000')},
    {'filename': 'portfolio-2.jpg', 'category': 'Blackwork', 'gradient': ('#0a0a0a', '#2a0000')},
    {'filename': 'portfolio-3.jpg', 'category': 'Illustrative', 'gradient': ('#1a1a1a', '#4a0000')},
    {'filename': 'portfolio-4.jpg', 'category': 'Color', 'gradient': ('#0a0000', '#6a0000')},
    {'filename': 'portfolio-5.jpg', 'category': 'Neo-Traditional', 'gradient': ('#2a2a2a', '#8B0000')},
    {'filename': 'portfolio-6.jpg', 'category': 'Blackwork', 'gradient': ('#0a0a0a', '#3a0000')},
    {'filename': 'portfolio-7.jpg', 'category': 'Illustrative', 'gradient': ('#1a1a1a', '#5a0000')},
    {'filename': 'portfolio-8.jpg', 'category': 'Large Scale', 'gradient': ('#0a0000', '#7a0000')},
    {'filename': 'portfolio-9.jpg', 'category': 'Color', 'gradient': ('#2a2a2a', '#9a0000')},
    {'filename': 'portfolio-10.jpg', 'category': 'Neo-Traditional', 'gradient': ('#1a0000', '#8B0000')},
    {'filename': 'portfolio-11.jpg', 'category': 'Blackwork', 'gradient': ('#0a0a0a', '#4a0000')},
    {'filename': 'portfolio-12.jpg', 'category': 'Large Scale', 'gradient': ('#1a1a1a', '#8B0000')},
]

# Flash designs data
flash_designs = [
    {'filename': 'flash-1.jpg', 'title': 'Raven Skull', 'gradient': ('#0a0a0a', '#8B0000')},
    {'filename': 'flash-2.jpg', 'title': 'Snake & Dagger', 'gradient': ('#1a0000', '#6a0000')},
    {'filename': 'flash-3.jpg', 'title': 'Geometric Wolf', 'gradient': ('#0a0a0a', '#5a0000')},
    {'filename': 'flash-4.jpg', 'title': 'Traditional Rose', 'gradient': ('#1a1a1a', '#8B0000')},
    {'filename': 'flash-5.jpg', 'title': 'Blackwork Moth', 'gradient': ('#0a0000', '#7a0000')},
    {'filename': 'flash-6.jpg', 'title': 'Surreal Eye', 'gradient': ('#2a2a2a', '#8B0000')},
    {'filename': 'flash-7.jpg', 'title': 'Demon Mask', 'gradient': ('#0a0a0a', '#4a0000')},
    {'filename': 'flash-8.jpg', 'title': 'Cosmic Cat', 'gradient': ('#1a0000', '#8B0000')},
]

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient(width, height, color1, color2):
    """Create vertical gradient from color1 to color2"""
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    
    # Create gradient mask
    for y in range(height):
        value = int(255 * (y / height))
        for x in range(width):
            mask.putpixel((x, y), value)
    
    base.paste(top, (0, 0), mask)
    return base

def generate_portfolio_image(data, output_path):
    """Generate a portfolio placeholder image"""
    width, height = 600, 800
    
    # Create gradient background
    rgb1 = hex_to_rgb(data['gradient'][0])
    rgb2 = hex_to_rgb(data['gradient'][1])
    img = create_gradient(width, height, rgb1, rgb2)
    
    draw = ImageDraw.Draw(img)
    
    # Add border
    border_color = (139, 0, 0)  # #8B0000
    border_width = 4
    draw.rectangle(
        [(0, 0), (width-1, height-1)],
        outline=border_color,
        width=border_width
    )
    
    # Add inner accent line
    inner_border = 12
    draw.rectangle(
        [(inner_border, inner_border), (width-inner_border, height-inner_border)],
        outline=border_color,
        width=2
    )
    
    # Add category text
    try:
        # Try to use a nice font (may not exist on all systems)
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    except:
        # Fallback to default
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw category text
    text = data['category'].upper()
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2 - 50
    
    # Draw text shadow
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), text, fill=(0, 0, 0, 180), font=font_large)
    
    # Draw main text
    draw.text((x, y), text, fill=(232, 232, 232, 200), font=font_large)
    
    # Add "PLACEHOLDER" label
    placeholder_text = "REPLACE WITH REAL IMAGE"
    bbox2 = draw.textbbox((0, 0), placeholder_text, font=font_small)
    text_width2 = bbox2[2] - bbox2[0]
    x2 = (width - text_width2) / 2
    y2 = y + text_height + 40
    
    draw.text((x2, y2), placeholder_text, fill=(160, 160, 160, 150), font=font_small)
    
    # Save
    img.save(output_path, 'JPEG', quality=90)
    print(f"✅ Created {output_path}")

def generate_flash_image(data, output_path):
    """Generate a flash design placeholder image"""
    width, height = 600, 600  # Square for flash
    
    # Create gradient background
    rgb1 = hex_to_rgb(data['gradient'][0])
    rgb2 = hex_to_rgb(data['gradient'][1])
    img = create_gradient(width, height, rgb1, rgb2)
    
    draw = ImageDraw.Draw(img)
    
    # Add border
    border_color = (139, 0, 0)
    border_width = 4
    draw.rectangle(
        [(0, 0), (width-1, height-1)],
        outline=border_color,
        width=border_width
    )
    
    # Add decorative corners
    corner_size = 30
    for corner in [(10, 10), (width-40, 10), (10, height-40), (width-40, height-40)]:
        draw.rectangle(
            [corner, (corner[0] + corner_size, corner[1] + corner_size)],
            outline=border_color,
            width=2
        )
    
    # Add title text
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 64)
        font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw title
    text = data['title'].upper()
    bbox = draw.textbbox((0, 0), text, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2 - 30
    
    # Text shadow
    draw.text((x + 2, y + 2), text, fill=(0, 0, 0, 180), font=font_large)
    # Main text
    draw.text((x, y), text, fill=(232, 232, 232, 200), font=font_large)
    
    # Add "FLASH DESIGN" label
    label_text = "FLASH DESIGN"
    bbox2 = draw.textbbox((0, 0), label_text, font=font_small)
    text_width2 = bbox2[2] - bbox2[0]
    x2 = (width - text_width2) / 2
    y2 = y + text_height + 30
    
    draw.text((x2, y2), label_text, fill=(160, 160, 160, 150), font=font_small)
    
    # Save
    img.save(output_path, 'JPEG', quality=90)
    print(f"✅ Created {output_path}")

def main():
    """Generate all placeholder images"""
    # Create images directory
    images_dir = 'images'
    os.makedirs(images_dir, exist_ok=True)
    
    print("🎨 Generating portfolio placeholders...")
    for data in portfolio_images:
        output_path = os.path.join(images_dir, data['filename'])
        generate_portfolio_image(data, output_path)
    
    print("\n🎨 Generating flash design placeholders...")
    for data in flash_designs:
        output_path = os.path.join(images_dir, data['filename'])
        generate_flash_image(data, output_path)
    
    print("\n✅ All placeholders generated!")
    print("\n📝 NEXT STEPS:")
    print("1. Replace placeholder images with real tattoo photos from @portergeist_art")
    print("2. Update tip jar links (Venmo/CashApp/PayPal handles)")
    print("3. Confirm contact email")
    print("4. Deploy to Vercel")

if __name__ == '__main__':
    main()
