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
