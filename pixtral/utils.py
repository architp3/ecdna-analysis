from PIL import Image
import zipfile
import os
import numpy as np
import random
import shutil
import pandas as pd
import cv2

from pydantic import BaseModel

class Count(BaseModel):
    count: int
    

def generate_random_sample(input_folder, output_folder, sample_size=200):
    """
        This function uses provided data and generates a random sample
        used for testing purposes.

        Inputs:
            input_folder: folder containing data
            output_folder: folder to write randomly sampled data
            sample_size: random sample size. Set to 200 by default
    """
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)
    
    images = []
    for f in os.listdir(input_folder):
        if f.endswith('.png'):
            images.append(f)
    
    sampled = random.sample(images, sample_size)

    for image in sampled:
        shutil.copy(os.path.join(input_folder, image), os.path.join(output_folder, image))
        
    sampled_df = pd.DataFrame(sampled, columns=['img'])
    return sampled_df

def read_red_channel(img_path):
    """
        This function filters the blue channel from images
        and generates a greyscale image highlighting the
        blue channel information.

        Input:
            img_path: path of image to be converted
        Output:
            Greyscaled image containing blue channel
    """
    image = cv2.imread(img_path)
    red_channel = image[:, :, 2]
    red_rgb = np.stack([red_channel, red_channel, red_channel], axis=-1)
    return Image.fromarray(red_rgb)

def read_green_channel(img_path):
    """
        This function filters the blue channel from images
        and generates a greyscale image highlighting the
        blue channel information.

        Input:
            img_path: path of image to be converted
        Output:
            Greyscaled image containing blue channel
    """
    image = cv2.imread(img_path)
    green_channel = image[:, :, 1]
    green_rgb = np.stack([green_channel, green_channel, green_channel], axis=-1)
    return Image.fromarray(green_rgb)

def read_blue_channel(img_path):
    """
        This function filters the blue channel from images
        and generates a greyscale image highlighting the
        blue channel information.

        Input:
            img_path: path of image to be converted
        Output:
            Greyscaled image containing blue channel
    """
    image = cv2.imread(img_path)
    blue_channel = image[:, :, 0]
    blue_rgb = np.stack([blue_channel, blue_channel, blue_channel], axis=-1)
    return Image.fromarray(blue_rgb)

def red_green_channel(img_path):
    image = cv2.imread(img_path)
    image[:, :, 0] = 0
    return Image.fromarray(image)
