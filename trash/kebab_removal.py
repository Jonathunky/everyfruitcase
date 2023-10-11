from PIL import Image
import numpy as np
import os


def remove_white_background(input_path, output_path):
    # Open the image
    img = Image.open(input_path)

    # Convert image to RGBA (so we can handle transparency)
    img = img.convert("RGBA")

    # Convert to numpy array
    data = np.array(img)

    # Create a white image of the same shape
    white = [255, 255, 255, 255]

    # Set transparency for white pixels
    data[(data == white).all(axis=-1)] = [255, 255, 255, 0]

    # Convert back to image and save
    output_img = Image.fromarray(data)
    output_img.save(output_path, "PNG")


def batch_process(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(
                directory, os.path.splitext(filename)[0] + ".png"
            )
            remove_white_background(input_path, output_path)


if __name__ == "__main__":
    dir_path = input("Enter directory path: ")
    batch_process(dir_path)
