import os
from PIL import Image

def remove_background(image_path, output_path, tolerance=40):
    img = Image.open(image_path).convert("RGBA")
    data = img.getdata()

    # Determine background color from top-left pixel
    bg_color = data[0][:3]  # (R, G, B)

    new_data = []
    for item in data:
        r, g, b, a = item
        # Calculate color difference from background
        diff = abs(r - bg_color[0]) + abs(g - bg_color[1]) + abs(b - bg_color[2])
        if diff < tolerance:
            new_data.append((0, 0, 0, 0))  # Transparent
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Saved transparent image to {output_path}")

brain_dir = r"C:\Users\user\.gemini\antigravity\brain\2752afba-d740-41ee-8498-01ae6aff4ade"
assets_dir = r"C:\Users\user\.gemini\antigravity\scratch\arc-pixel-farm\assets"

os.makedirs(assets_dir, exist_ok=True)

# Farmer Spritesheet
farmer_img_path = os.path.join(brain_dir, "farmer_spritesheet_v2_1785741058531.jpg")
if os.path.exists(farmer_img_path):
    remove_background(farmer_img_path, os.path.join(assets_dir, "farmer_trans.png"), tolerance=45)

# Crops Spritesheet
crops_img_path = os.path.join(brain_dir, "crops_spritesheet_1785741068361.jpg")
if os.path.exists(crops_img_path):
    remove_background(crops_img_path, os.path.join(assets_dir, "crops_trans.png"), tolerance=45)
