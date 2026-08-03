from PIL import Image

img = Image.open(r"C:\Users\user\Downloads\Sprout Lands - Sprites - Basic pack\Sprout Lands - Sprites - Basic pack\Objects\Free_Chicken_House.png")
print("Free_Chicken_House.png size:", img.size)

img.save('chicken_house_building.png')
print("chicken_house_building.png saved!")
