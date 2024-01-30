import Augmentor
import argparse

# Function to perform data augmentation
def augment_data(input_dir, output_dir, num_samples, rotate, flip, scale, contrast, brightness, shear, translate, grayscale, blur, noise, color, equalize, erasing ):
    p = Augmentor.Pipeline(input_dir, output_directory=output_dir)

    if rotate:
        p.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
    if flip:
        p.flip_left_right(probability=0.5)
        p.flip_top_bottom(probability=0.5)
    if scale:
        p.zoom_random(probability=0.5, percentage_area=0.8)
    if contrast:
        p.random_contrast(probability=0.5, min_factor=0.5, max_factor=2.0)
    if brightness:
        p.random_brightness(probability=0.5, min_factor=0.7, max_factor=1.3)
    if shear:
        p.shear(probability=0.4, max_shear_left=25, max_shear_right=25)
    if translate:
        p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
    if grayscale:
        p.random_grayscale(probability=0.5)
    if color:
         p.random_color(probability=0.5, min_factor=0.8, max_factor=1.2)
    if equalize:
        p.histogram_equalisation(probability=0.5)
    if blur:
        p.gaussian_blur(probability=0.5, min_sigma=0.5, max_sigma=1)
    if noise:
        p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)
    if erasing:
        p.random_erasing(probability=0.5, rectangle_area=0.3)


    p.sample(num_samples)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Augmentation with Augmentor")
    parser.add_argument("--input_dir", type=str, required=True, help="Input directory containing images")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory for augmented images")
    parser.add_argument("--num_samples", type=int, default=100, help="Number of augmented samples to generate")
    parser.add_argument("--rotate", action="store_true", help="Apply random rotation")
    parser.add_argument("--flip", action="store_true", help="Apply random flip")
    parser.add_argument("--scale", action="store_true", help="Apply random scaling")
    parser.add_argument("--contrast", action="store_true", help="Apply random contrast adjustment")
    parser.add_argument("--brightness", action="store_true", help="Apply random brightness adjustment")
    parser.add_argument("--shear", action="store_true", help="Apply random shear")
    parser.add_argument("--translate", action="store_true", help="Apply random translation")
    parser.add_argument("--blur", action="store_true", help="Apply random blur")
    parser.add_argument("--grayscale", action="store_true", help="Apply random grayscale")
    parser.add_argument("--color", action="store_true", help="Apply random color")
    parser.add_argument("--noise", action="store_true", help="Add salt and pepper noise")
    parser.add_argument("--erasing", action="store_true", help="Apply random erasing")
    parser.add_argument("--equalize", action="store_true", help="Apply histogram equalization")

    args = parser.parse_args()

    augment_data(args.input_dir, args.output_dir, args.num_samples, args.rotate, args.flip, args.scale, args.contrast, args.brightness, args.shear, args.translate,args.blur, args.grayscale, args.color, args.erasing, args.noise, args.equalize)
