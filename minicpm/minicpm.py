import torch

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import csv

from PIL import Image
from transformers import AutoModel, AutoTokenizer
from torchvision import transforms
from tqdm import tqdm
from IPython.display import display

def save_to_csv(context, question, image_str, output, filename='output.csv'):
    # Check if the file already exists
    file_exists = os.path.isfile(filename)
    
    # Open the file in append mode, create if it doesn't exist
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        # If the file does not exist, write the headers
        if not file_exists:
            writer.writerow(['Context', 'Question', 'Image_Path', 'Output'])
            file_exists = True
        # Write the data row
        writer.writerow([context, question, image_str, output])

def test_model(file_path, img_path, model, tokenizer, qcontext, question, filename, img_path2 = None, question2 = None):
    model.eval()
    msgs = [{'role': 'user', 'content': question}]

    full_image = os.path.join(file_path, img_path)
    # _, _, img = Image.open(full_image).convert('RGB').split()
    img = Image.open(full_image).convert('RGB')
    
    res, context, _ = model.chat(
        image=img,
        msgs=msgs,
        context=qcontext,
        tokenizer=tokenizer,
        sampling=True,
        temperature=1
    )
    save_to_csv(qcontext, question, img_path, res, filename + ".csv")

    if img_path2:
        msgs.append({"role": "assistant", "content": res})
        msgs.append({"role": "user", "content": question2})

        full_image = os.path.join(file_path, img_path2)
        # _, _, img = Image.open(full_image).convert('RGB').split()
        img = Image.open(full_image).convert('RGB')
        
        res, context, _ = model.chat(
            image=img,
            msgs=msgs,
            context=qcontext,
            tokenizer=tokenizer,
            sampling=True,
            temperature=1
        )

        return res, img
        
    return res, img