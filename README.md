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
This will be the file containing all the fields required and optional fields for model inputs. To generate this file, run the following command: </br>

```
copy config_copy.yaml config.yaml
```


#### Qwen2-VL Parameters

The following field is provided for users who do not have enough disk space and would like to download certain files from the entire dataset: </br>

`zipfile_path`: path to folder containing the ecSeg_dataset downloaded data.</br>
`test_extract_folder`: New path containing the extracted train images.<br />
`train_extract_folder`: New path containing the extracted train images.<br />

The fields have been filled out for you in the `config_copy.yaml` file:</br>
`test_folder_name`: name of test folder in the ecSeg data folder (stored as `test_im`).<br />
`train_folder_name`: name of train folder in the ecSeg data folder (stored as `train_im`).<br />

The following fields are required:</br>

`sampled`: File to store randomly sampled images. <br/>
`sample_size`: Sample size for random sampling. Set to 200 by default.<br/>

Once the data has been populated in the repository, use the following terminal command to setup random sampling and zipfile extraction if not already done:

```
pythons setup.py --extract-zip y
```
Use 'y' if you want to conduct zip extraction and 'n' otherwise.
