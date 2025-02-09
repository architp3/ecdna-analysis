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

### Config file

#### Qwen2-VL Parameters
`zipfile_path`: path to folder containing the ecSeg_dataset downloaded data.
`test_folder_name`: name of test folder in the ecSeg data folder (test_im).
`test_extract_folder`: New path containing the extracted train images.
`train_folder_name`: name of train folder in the ecSeg data folder (train_im).
`train_extract_folder`: New path containing the extracted train images.
