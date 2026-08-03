import os
import shutil

sprites_dir = r"C:\Users\user\Downloads\Sprout Lands - Sprites - Basic pack"
ui_dir = r"C:\Users\user\Downloads\Sprout Lands - UI Pack - Basic pack"

found_files = {}
for root, dirs, files in os.walk(sprites_dir):
    for f in files:
        found_files[f.lower()] = os.path.join(root, f)

for root, dirs, files in os.walk(ui_dir):
    for f in files:
        found_files[f.lower()] = os.path.join(root, f)

sprout_assets = {
    "basic_character.png": "basic charakter spritesheet.png",
    "basic_character_actions.png": "basic charakter actions.png",
    "chicken_sprites.png": "free chicken sprites.png",
    "cow_sprites.png": "free cow sprites.png",
    "basic_plants.png": "basic plants.png",
    "grass.png": "grass.png",
    "tilled_dirt.png": "tilled dirt.png",
    "water.png": "water.png",
    "wooden_house.png": "wooden house.png",
    "fences.png": "fences.png",
    "chest.png": "chest.png",
    "egg_item.png": "egg item.png",
    "milk_item.png": "simple milk and grass item.png",
    "paths.png": "paths.png",
    "wood_bridge.png": "wood bridge.png",
    "tools.png": "tools.png"
}

for dest_name, src_name in sprout_assets.items():
    if src_name in found_files:
        shutil.copy(found_files[src_name], dest_name)
        print(f"Successfully copied {src_name} -> {dest_name}")
    else:
        print(f"Could not find {src_name}")

print("All Sprout Lands official assets ready in project folder!")
