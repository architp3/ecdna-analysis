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
Dataset used for analysis can be found <a href='https://data.mendeley.com/datasets/m7n3zvg539/4'> here <\a>


### Configuration File (config.yaml)
This will be the file containing all the fields required for model inputs.

#### Qwen2-VL Parameters
`zipfile_path`: path to folder containing the ecSeg_dataset downloaded data.<br />
`test_folder_name`: name of test folder in the ecSeg data folder (stored as `test_im`).<br />
`test_extract_folder`: New path containing the extracted train images.<br />
`train_folder_name`: name of train folder in the ecSeg data folder (stored as `train_im`).<br />
`train_extract_folder`: New path containing the extracted train images.<br />
