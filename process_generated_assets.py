from PIL import Image, ImageChops
import os

# 1. Process Tudor House Background Transparency
house = Image.open('stardew_house.jpg').convert('RGBA')
datas = house.getdata()

# Find edge background color (around top-left pixel)
bg_color = datas[0]

newData = []
for item in datas:
    # Calculate color distance to background color
    dist = abs(item[0] - bg_color[0]) + abs(item[1] - bg_color[1]) + abs(item[2] - bg_color[2])
    if dist < 45:
        newData.append((0, 0, 0, 0)) # Make transparent
    else:
        newData.append(item)

house.putdata(newData)
house.save('house_clean.png')
print("house_clean.png created!")

# 2. Extract Individual Tiles from Tileset Image
tileset = Image.open('stardew_tileset.jpg')
w, h = tileset.size

# Sub-crop regions
grass = tileset.crop((0, 0, w//2, h//2))
grass.save('tile_grass.png')

tilled = tileset.crop((w//2, 0, w, h//2))
tilled.save('tile_tilled.png')

path = tileset.crop((0, h//2, w//2, h))
path.save('tile_path.png')

water = tileset.crop((w//2, h//2, w, h))
water.save('tile_water.png')

print("All extracted clean tile assets saved successfully!")
