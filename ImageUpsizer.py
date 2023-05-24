import os
import argparse
from PIL import Image

# Command-line argument parser
parser = argparse.ArgumentParser(description='Upsize images in a directory.')
parser.add_argument('-i', '--input', help='Path to the input directory', required=True)
parser.add_argument('-o', '--output', help='Path to the output directory', required=True)
parser.add_argument('-s', '--size', type=int, help='Minimum size for the shortest dimension of the image', required=True)
parser.add_argument('-u', '--use', choices=['web', 'print'], help='Intended use for the upsized image', required=True)
args = parser.parse_args()

# Folder containing the original images
input_folder = args.input

# Output folder for upsized images
output_folder = args.output

# Min size for the shortest dimension of the image
min_size = args.size

# Intended use for the upsized image
intended_use = args.use

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    print('Creating output directory:', output_folder)
    os.mkdir(output_folder)

# Supported image file formats
img_formats = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.ico']

# Loop through all files in the original directory
print('Starting upsizing process...')
for filename in os.listdir(input_folder):
    if os.path.splitext(filename)[1].lower() in img_formats:
        print('Processing', filename)
        
        try:
            img = Image.open(os.path.join(input_folder, filename))
        except IOError:
            print(f'Error opening image {filename}. Skipping...')
            continue
        
        # Only upsize if image is smaller than the required size
        if min(img.size[0], img.size[1]) < min_size:
            ratio = min_size / min(img.size[0], img.size[1])
            new_dimensions = (int(img.size[0]*ratio), int(img.size[1]*ratio))
            
            # Use different filters for web and print
            if intended_use == 'web':
                img = img.resize(new_dimensions, Image.NEAREST)
            else:  # intended_use == 'print'
                img = img.resize(new_dimensions, Image.LANCZOS)
        else:
            print(f'Image {filename} is already larger than the target size. Skipping...')
            continue
        
        # Split the filename into name and extension, add suffix to the name
        base_name, extension = os.path.splitext(filename)
        output_filename = f"{base_name}_upsized{extension}"
        
        try:
            img.save(os.path.join(output_folder, output_filename))
            print(f'Saved upsized image as: {output_filename}')
        except IOError:
            print(f'Error saving image {filename}. Skipping...')
            continue
        finally:
            img.close()

print('Upsizing completed.')
