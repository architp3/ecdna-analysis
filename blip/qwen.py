from PIL import Image
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor, BlipProcessor, BlipForConditionalGeneration, pipeline
from qwen_vl_utils import process_vision_info
import gradio as gr
import zipfile
import os
import numpy as np
import random
import shutil
import pandas as pd
import cv2

# Zipfile path containing data
zipfile_path = os.path.expanduser("~") + '\\ecdna-analysis\\data\\ecSeg_dataset.zip'

def extract_zip_path(zip_file_path, folder_name, extract_folder):
        # Folder inside the ZIP file that contains the images
        

        # Open the ZIP file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            all_files = zip_ref.namelist()
            
            # Filter image files from the specified folder
            image_files = [f for f in all_files if f.find(folder_name) != -1]
            
            for image_file in image_files:
                # Extract the file to the extraction folder
                zip_ref.extract(image_file, extract_folder)
                
                # Check if the file is a TIFF image (ends with .tif)
                if image_file.lower().endswith('.tif'):
                    # Construct the local path for the TIFF file and the destination path
                    extracted_tiff_path = os.path.join(extract_folder, image_file)
            
        zip_ref.close()

def generate_random_sample(input_folder, output_folder):
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)
    
    images = [f for f in os.listdir(input_folder)]
    sampled = random.sample(images, 200)

    for image in sampled:
        shutil.copy(os.path.join(input_folder, image), os.path.join(output_folder, image))
        
    return pd.DataFrame(sampled)

def read_blue_channel(img_path):
    image = cv2.imread(img_path)
    blue_channel = image[:, :, 0]
    blue_rgb = np.stack([blue_channel, blue_channel, blue_channel], axis=-1)

    return Image.fromarray(blue_rgb)