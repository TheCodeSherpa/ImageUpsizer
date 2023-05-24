# Image Upsizer

## Introduction
"TheCodeSherpa" brings to you an efficient Python script to upsize images while maintaining their original aspect ratio. This utility stands out due to its ability to optimize the upsizing process based on the intended use of the output images. You can specify whether the upsized image is intended for web display or print, and the script will apply the most suitable algorithm for each scenario.

Additionally, the script supports a variety of image formats, such as JPEG, PNG, TIFF, BMP, and ICO, and comes equipped with improved error handling to tackle potential issues like inability to open or save files, or non-existing input directories.

## Requirements
Python 3.x is necessary to run this script, along with the following Python packages:

- os
- argparse
- PIL (Python Imaging Library)

These packages can be installed with pip:

```bash
pip install pillow argparse
```

## Usage
Use the script from the command line with the following command:

```bash
python image_upsizer.py -i input_directory -o output_directory -s min_size -u use
```

Where:

- `-i` or `--input`: Path to the input directory containing the images you want to upsize.
- `-o` or `--output`: Path to the output directory where the upsized images will be saved. If the directory doesn't exist, the script will create it.
- `-s` or `--size`: Minimum size for the shortest dimension of the upsized images.
- `-u` or `--use`: Intended use for the upsized image. Accepts either "web" or "print".

For instance, if you need to upsize images in the directory `/path/to/images`, save them in `/path/to/output`, with a minimum size of 1200, and you intend to use them for print, you would use:

```bash
python image_upsizer.py -i /path/to/images -o /path/to/output -s 1200 -u print
```

The script will upsize all supported images in the input directory, skipping any images that are already larger than the target size, and save the resulting images in the output directory. The filename for each upsized image will include `_upsized` appended to the original filename.

## Contributing
Your contributions are always welcome! Please feel free to submit pull requests or open issues if you want to contribute to the project. Make sure that your code includes appropriate comments that explain any modifications or additions you've made.

## License
This project is open-source and freely available under the [MIT License](LICENSE).