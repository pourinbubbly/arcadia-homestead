from PIL import Image

img = Image.open('wooden_house.png')
print("wooden_house.png dimensions:", img.size)

# Create a clean composite Sprout house sprite using its tileset pieces!
# Sprout house tileset: 112x80 (7 tiles wide x 5 tiles high, each 16x16)
house_composite = Image.new('RGBA', (64, 64), (0, 0, 0, 0))

# Roof top row
house_composite.paste(img.crop((0, 0, 16, 16)), (16, 0))
house_composite.paste(img.crop((16, 0, 32, 16)), (32, 0))

# Wall row
house_composite.paste(img.crop((0, 16, 16, 32)), (16, 16))
house_composite.paste(img.crop((16, 16, 32, 32)), (32, 16))

# Door row
house_composite.paste(img.crop((0, 32, 16, 48)), (16, 32))
house_composite.paste(img.crop((16, 32, 32, 48)), (32, 32))

house_composite.save('sprout_house_building.png')
print("sprout_house_building.png composite created!")
