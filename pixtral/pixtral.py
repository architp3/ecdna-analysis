# %% [markdown]
# ## Extract and Prep Data

# %%
from PIL import Image
import zipfile

import base64
import os
import requests

from mistralai import Mistral

# %%
# Helper function
def convert_tiff_to_png(tiff_path, png_path):
    with Image.open(tiff_path) as img:
        img.save(png_path, 'PNG')

# %%
zip_file_path = 'data/ecSeg_dataset.zip'

# Folder inside the ZIP file that contains the images
folder_name = 'test_im/'

# Folder to extract converted images
extract_folder = 'data/jpgs/'

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

# %% [markdown]
# ## Demo Run
# 
# We will be prompting the `Pixtral-12b` model with the following metaphase image of a cell:
# 
# ![alt text](data/converted/19.jpg "Metaphase Image of Cell")
# 
# And the following prompt:
# 
# "For this task, act as a bioligist who is studying extrachromosomal DNA (ecDNA). Consider this metaphase image containing ecDNA. Analyze it for possible ecDNA."

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

# %% [markdown]
# ### Setup Model

# %%
api_key = "jPj7kLzhpj8aicxtA9cpyDg1uP50zvtW"

# Specify model
model = "pixtral-large-latest"

# Path to your image
image_path = "data/converted/19.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

client = Mistral(api_key=api_key)

# %% [markdown]
# ### Analyze metaphase images

# %%
# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "For this task, act as a bioligist who is studying extrachromosomal DNA (ecDNA). Consider this metaphase image containing ecDNA. Analyze it for possible ecDNA."
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

# %% [markdown]
# ### Count number of chromosomes

# %%
# Path to your image
image_path = "data/converted/2314.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "For this task, act as a bioligist who is studying extrachromosomal DNA (ecDNA). Consider this metaphase image containing ecDNA. Count how many chromosomes are present in the image."
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

# %%
# Path to your image
image_path = "data/converted/19.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "For this task, act as a bioligist who is studying extrachromosomal DNA (ecDNA). Consider this metaphase image containing ecDNA. Count how many nuclei are present in the image."
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

# %%
# Save output
with open("output.txt", "w") as file:
    file.write(chat_response.choices[0].message.content)

# %% [markdown]
# ## Conclusions
# As we can see from the above input, the Pixtral-12b model is able to provide a quite detailed and somewhat coherent explanation of the image. It is able to reason why certain parts of the image are colored the way they are such as discussing relevant methods used to stain DNA.


