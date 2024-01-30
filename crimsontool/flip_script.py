# flip_script.py

import sys
import os
from PIL import Image

def flip_image(image_path):
    try:
        original_img = Image.open(image_path)

        if original_img.mode == 'RGBA':
            original_img = original_img.convert('RGB')

        flipped_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)

        root, ext = os.path.splitext(image_path)

        flipped_image_path = f"{root}_flipped{ext}"

        flipped_img.save(flipped_image_path)
        return flipped_image_path

    except Exception as e:
        print("Error flipping image: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python flip_script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    flipped_image_path = flip_image(image_path)

    if flipped_image_path:
        print(flipped_image_path)
    else:
        sys.exit(1) 