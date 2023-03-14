from PIL import Image
import os 

for image_name in os.listdir("images"):
    if ".png" in image_name:
        im = Image.open(f"images/{image_name}")
        rgb_im = im.convert('RGB')
        rgb_im.save(f'images/{image_name.replace(".png", "")}.jpg')