from PIL import Image
import gradio as gr
import zipfile
import os
import numpy as np
import random
import shutil
import pandas as pd
import cv2
import argparse
import yaml

# Zipfile path containing data
def extract_zip_path(zip_file_path, folder_name, extract_folder):
        """
            This function extracts certain folders from the ecSeg zipfile.
            
            Input:
                zip_file_path: Path to zipfile containing all the data
                folder_name: Name of the folder that you want to extract from ecSeg.
                extract_folder: file to save all the extracted images 
        """
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
    
    images = [f for f in os.listdir(input_folder)]
    print(len(images))
    sampled = random.sample(images, sample_size)

    for image in sampled:
        shutil.copy(os.path.join(input_folder, image), os.path.join(output_folder, image))
        
    return pd.DataFrame(sampled)

def main():
    HOME = os.path.expanduser('~') + "\\ecdna-analysis"
    config_path = os.path.join(HOME, "config.yaml")
    config = open(config_path)

    var = yaml.load(config, Loader=yaml.FullLoader)['qwen']

    zip_file_path = os.path.join(HOME, var['zipfile_path'])
    test_folder_name = var['test_folder_name']
    test_extract_folder = os.path.join(HOME, var['test_extract_folder'])
    train_folder_name = var['train_folder_name']
    train_extract_folder = os.path.join(HOME, var['train_extract_folder'])

    print(f"Train folder path: {train_extract_folder}")
    print(f"Test folder name: {test_extract_folder}")

    sample_size = var['sample_size']
    input_folder = os.path.join(test_extract_folder , f'ecSeg_dataset\\{test_folder_name}')
    output_folder = os.path.join(HOME, var['sampled'] )

    parser = argparse.ArgumentParser(description='Setup script for extracting and sampling data.')
    parser.add_argument('--extract_zip', choices=['y', 'n'], required=True, help="Whether to extract the zip file. 'y' or 'n'")
    args = parser.parse_args()

    
    if args.extract_zip.lower() == 'y':
        print('Extracting zip file')
        extract_zip_path(zip_file_path, train_folder_name, train_extract_folder)
        extract_zip_path(zip_file_path, test_folder_name, test_extract_folder)
    else:
        print('Skipping zipfile extraction.')
    
    print('Generating random sample...')
    generate_random_sample(input_folder, output_folder, sample_size=sample_size)
    print('Random sample generated')


if __name__ == '__main__':
    main()
