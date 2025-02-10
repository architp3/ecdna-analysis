# ecDNA Analysis

Our data is collected from the following sources:
- https://data.mendeley.com/datasets/m7n3zvg539/4
- https://www.nature.com/articles/s41597-023-02003-7

# Setup Instructions
### Virtual Environment
```
conda create --name ecdna
conda activate ecdna
pip install pillow gradio transformers os zipfile yaml
pip install --upgrade opencv-python
```

For Qwen2-VL Model, install the following additional packages:
```
pip install qwen_vl_utils
```

For Pixtral Large Model, install the following additional packages:
```
pip install mistralai
```

For MiniCPM-V2, no additional packages are needed

### Dataset

Sampled data of 200 images is provided in this repository. For users with interest in further exploration the dataset can be found <a href='https://data.mendeley.com/datasets/m7n3zvg539/4'> here </a>. </br>

Once the dataset is downloaded, unzip the data and add it to your repository. The data format once downloaded will be in the following format:

```
ecSeg_dataset
|
|--full_images
|--test_im
|--test_mask
|--train_im
|--train_mask
```

### Configuration File (config.yaml)
This will be the file containing all the fields required and optional fields for model inputs.

#### Qwen2-VL Parameters

The following fields are provided for users for do not have enough disk space and can extract data directly from the zip file:

`zipfile_path`: path to folder containing the ecSeg_dataset downloaded data.<br />
`test_folder_name`: name of test folder in the ecSeg data folder (stored as `test_im`).<br />
`test_extract_folder`: New path containing the extracted train images.<br />
`train_folder_name`: name of train folder in the ecSeg data folder (stored as `train_im`).<br />
`train_extract_folder`: New path containing the extracted train images.<br />
`sampled`

After these fields have been populated, run `python setup.py` in order to load data into the repository.
