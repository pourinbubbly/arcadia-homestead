from PIL import Image

files = [
    'grass.png', 'wooden_house.png', 'tilled_dirt.png',
    'basic_character.png', 'basic_plants.png',
    'chicken_sprites.png', 'cow_sprites.png', 'fences.png'
]

for f in files:
    try:
        img = Image.open(f)
        print(f"{f}: size = {img.size}, mode = {img.mode}")
    except Exception as e:
        print(f"Error opening {f}: {e}")
