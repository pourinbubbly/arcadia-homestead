from PIL import Image, ImageDraw
import os

# 1. Create Transparent Farmer Spritesheet (4 directions x 3 walk frames = 12 frames, each 32x32)
farmer_img = Image.new('RGBA', (96, 128), (0, 0, 0, 0))
draw = ImageDraw.Draw(farmer_img)

# Direction rows: 0=Down, 1=Up, 2=Left, 3=Right
dirs = ['down', 'up', 'left', 'right']

for d_idx, d in enumerate(dirs):
    for f_idx in range(3):
        fx = f_idx * 32
        fy = d_idx * 32
        leg_offset = (f_idx % 2) * 2

        # Shadow
        draw.ellipse([fx + 8, fy + 26, fx + 24, fy + 31], fill=(0, 0, 0, 100))
        
        # Boots
        draw.rectangle([fx + 10 - leg_offset, fy + 24, fx + 15 - leg_offset, fy + 29], fill=(69, 26, 3, 255))
        draw.rectangle([fx + 17 + leg_offset, fy + 24, fx + 22 + leg_offset, fy + 29], fill=(69, 26, 3, 255))

        # Blue Overalls / Pants
        draw.rectangle([fx + 10, fy + 18, fx + 22, fy + 25], fill=(29, 78, 216, 255))
        
        # Red Plaid Shirt
        draw.rectangle([fx + 8, fy + 10, fx + 24, fy + 19], fill=(220, 38, 38, 255))
        draw.rectangle([fx + 11, fy + 10, fx + 21, fy + 18], fill=(185, 28, 28, 255)) # Inner plaid

        # Head / Skin
        draw.rectangle([fx + 10, fy + 4, fx + 22, fy + 12], fill=(253, 224, 71, 255))
        
        # Eyes
        if d == 'down':
            draw.rectangle([fx + 12, fy + 7, fx + 14, fy + 9], fill=(0, 0, 0, 255))
            draw.rectangle([fx + 18, fy + 7, fx + 20, fy + 9], fill=(0, 0, 0, 255))
        elif d == 'left':
            draw.rectangle([fx + 11, fy + 7, fx + 13, fy + 9], fill=(0, 0, 0, 255))
        elif d == 'right':
            draw.rectangle([fx + 19, fy + 7, fx + 21, fy + 9], fill=(0, 0, 0, 255))

        # Straw Hat
        draw.rectangle([fx + 4, fy + 2, fx + 28, fy + 5], fill=(234, 179, 8, 255))
        draw.rectangle([fx + 8, fy + 0, fx + 24, fy + 3], fill=(202, 138, 4, 255))

farmer_img.save('farmer_sprite.png')

# 2. Create Tudor House Sprite (160x160 Transparent PNG)
house_img = Image.new('RGBA', (160, 160), (0, 0, 0, 0))
h_draw = ImageDraw.Draw(house_img)

# Stone foundation
h_draw.rectangle([10, 100, 150, 140], fill=(71, 85, 105, 255))
for x in range(12, 148, 16):
    h_draw.rectangle([x, 104, x + 12, 116], fill=(100, 116, 139, 255))
    h_draw.rectangle([x + 6, 120, x + 18, 134], fill=(100, 116, 139, 255))

# Cream Plaster Wall
h_draw.rectangle([16, 20, 144, 100], fill=(254, 243, 199, 255))

# Timber Beams
beam_color = (69, 26, 3, 255)
h_draw.rectangle([16, 20, 144, 26], fill=beam_color)
h_draw.rectangle([16, 56, 144, 62], fill=beam_color)
h_draw.rectangle([16, 94, 144, 100], fill=beam_color)
h_draw.rectangle([16, 20, 22, 100], fill=beam_color)
h_draw.rectangle([138, 20, 144, 100], fill=beam_color)
h_draw.rectangle([77, 20, 83, 100], fill=beam_color)

# Windows with Glow
h_draw.rectangle([30, 32, 60, 50], fill=(30, 41, 59, 255))
h_draw.rectangle([32, 34, 58, 48], fill=(254, 240, 138, 255))
h_draw.rectangle([100, 32, 130, 50], fill=(30, 41, 59, 255))
h_draw.rectangle([102, 34, 128, 48], fill=(254, 240, 138, 255))

# Flower window box
h_draw.rectangle([26, 50, 64, 55], fill=(120, 53, 15, 255))
h_draw.rectangle([96, 50, 134, 55], fill=(120, 53, 15, 255))
for fx in range(28, 62, 8):
    h_draw.rectangle([fx, 47, fx + 5, 51], fill=(236, 72, 153, 255))
for fx in range(98, 132, 8):
    h_draw.rectangle([fx, 47, fx + 5, 51], fill=(168, 85, 247, 255))

# Slate Purple Roof
h_draw.polygon([(0, 20), (80, -40), (160, 20)], fill=(59, 45, 84, 255))
h_draw.polygon([(6, 18), (80, -34), (154, 18)], fill=(88, 68, 125, 255))

# Arched Oak Door
h_draw.rectangle([66, 96, 94, 136], fill=beam_color)
h_draw.rectangle([69, 99, 91, 133], fill=(120, 53, 15, 255))
h_draw.rectangle([85, 114, 89, 118], fill=(245, 158, 11, 255))

house_img.save('house.png')

# 3. Create Oak & Pine Tree Sprites (64x96 Transparent PNGs)
tree_img = Image.new('RGBA', (128, 96), (0, 0, 0, 0))
t_draw = ImageDraw.Draw(tree_img)

# Oak Tree (Left side: 0..64)
t_draw.rectangle([24, 48, 40, 90], fill=(69, 26, 3, 255))
t_draw.rectangle([28, 52, 36, 86], fill=(120, 53, 15, 255))
t_draw.ellipse([8, 0, 56, 48], fill=(22, 101, 52, 255))
t_draw.ellipse([4, 12, 44, 52], fill=(21, 128, 61, 255))
t_draw.ellipse([20, 12, 60, 52], fill=(34, 197, 94, 255))
t_draw.ellipse([12, 4, 52, 44], fill=(74, 222, 128, 255))

# Pine Tree (Right side: 64..128)
t_draw.rectangle([90, 54, 102, 90], fill=(69, 26, 3, 255))
t_draw.polygon([(96, 0), (70, 36), (122, 36)], fill=(6, 78, 59, 255))
t_draw.polygon([(96, 20), (66, 56), (126, 56)], fill=(4, 120, 87, 255))
t_draw.polygon([(96, 40), (62, 76), (130, 76)], fill=(16, 185, 129, 255))

tree_img.save('trees.png')

print("All modular PNG pixel art assets generated successfully!")
