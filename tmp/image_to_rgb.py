"""
Generates a new jpeg 8-bit greyscale single channel image for every one in PATH_TO_IMAGES_INPUT folder.
Writes new images to PATH_TO_IMAGES_OUTPUT
"""
from PIL import Image
import os

PATH_TO_IMAGES_INPUT = 'input'
PATH_TO_IMAGES_OUTPUT = "output"
EXTRACTION_DPI = 300

def image_to_rgb():
    """
    Transform every image in path into a png one for making it compatible with TF pre-trained NN
    :param img_path: path to image folder
    :return: None. It writes images on disk
    """

    from os import listdir
    from os.path import isfile, join
    image_names = [f for f in listdir(PATH_TO_IMAGES_INPUT) if isfile(join(PATH_TO_IMAGES_INPUT, f))]
    print(image_names)

    counter = 0
    for image_name in image_names:
        counter += 1
        image_path = os.path.join(PATH_TO_IMAGES_INPUT, image_name)
        print(image_path)
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            output_image_path = os.path.join(PATH_TO_IMAGES_OUTPUT, image_name)
            img.save(output_image_path, dpi=(EXTRACTION_DPI, EXTRACTION_DPI))

if __name__ == '__main__':
    image_to_rgb()
