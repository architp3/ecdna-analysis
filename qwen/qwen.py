from PIL import Image
import gradio as gr
import zipfile
import os
import numpy as np
import random
import shutil
import pandas as pd
import cv2
import sys

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