# %% [markdown]
# ## Extract and Prep Data

# %%
from PIL import Image
import zipfile

import base64
import os
import requests

from mistralai import Mistral
import tkinter as tk

# %%
# Helper function
def convert_tiff_to_png(tiff_path, png_path):
    with Image.open(tiff_path) as img:
        img.save(png_path, 'PNG')

# %%
def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

# %%
# Save output
def save(chat_response):
    with open("output.txt", "w") as file:
        file.write(chat_response.choices[0].message.content)


def load_data(zip_file_path, folder_name, extract_folder):

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
                # Construct the local path for the TIFF file and the destination PNG path
                extracted_tiff_path = os.path.join(extract_folder, image_file)
                png_path = os.path.join(extract_folder, f"{os.path.splitext(image_file)[0]}.jpg")
                
                # Convert the TIFF to PNG
                convert_tiff_to_png(extracted_tiff_path, png_path)
                
                # Optionally, remove the original TIFF file after conversion
                os.remove(extracted_tiff_path)
                print(f"Converted {image_file} to PNG.")

        print(f"Images extracted and converted to PNG in: {extract_folder}")
        
    zip_ref.close()
    
def prompt_model(image_path, txt_prompt):
    api_key = ""
    
    client = Mistral(api_key=api_key)
    
    # Specify model
    model = "pixtral-large-latest"
    
    # Getting the base64 string
    base64_image = encode_image(image_path)

    # Define the messages for the chat
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f'{txt_prompt}'
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
        }
    ]

    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )

    # Print the content of the response
    print(chat_response.choices[0].message.content)
    
def generate_labels(qwen_out, pixtral_out, cpm_out):
    
    def load_text(file_path, tw):
        with open(file_path, 'r') as file:
            data = file.read()
            tw.insert(tk.END, data)

    root = tk.Tk()
    root.title("LLM Outputs")

    blip_label = tk.Label(root, text='Qwen Output')
    blip_label.pack()

    text_widget_qwen = tk.Text(root, height=10, width=50)
    text_widget_qwen.pack()  

    w = tk.Label(root, text='Pixtral Large Output')
    w.pack()

    text_widget_pix = tk.Text(root, height=10, width=50)
    text_widget_pix.pack()
    
    cpm_label = tk.Label(root, text='MiniCPM Output')
    cpm_label.pack()

    text_widget_cpm = tk.Text(root, height=10, width=50)
    text_widget_cpm.pack()


    load_text(pixtral_out, text_widget_qwen)
    load_text(qwen_out, text_widget_pix)
    load_text(cpm_out, text_widget_cpm)


    root.mainloop()