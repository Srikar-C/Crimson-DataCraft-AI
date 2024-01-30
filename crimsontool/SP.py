# your_image_script.py

from PIL import Image
import sys





def process_image(image_path):
    try:
        # Open and process the image (replace this with your actual image processing logic)    
        img = Image.open(image_path)
        name = image_path.split('/')[2]



        # Rotate the image
        # rotated_img = img.rotate(degrees)
        flip_Img = img.rotate(angle=90,expand=True);
        rotated_img = flip_Img.convert('RGB')
        path = rotated_img.save('media/rotatedImages/'+'rotated_'+name)



        # rda = rotate_Img(image='rotatedImages/'+'rotated_'+name)
        # rda.save() 
        if rotated_img:
            print('rotatedImages/'+'rotated_'+name)
        else:
            print('None')

    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python your_image_script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    path=process_image(image_path)


if __name__ == "__main__":
    # from .models import rotate_Img
    main()
