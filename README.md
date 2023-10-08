# Background Removal API Using Deep Learning Tool

- Here i am creating a FastAPI for removes the Background of an Images using Python And pre-trained AI/ML models
    which accepts images with .jpg and .png extension.

## Steps That I follow to develope this task.

- There is a one python library or we can say a project or a tool that can help us to remove background of an image files
- https://github.com/danielgatis/rembg

- It uses the u2net: salienct object detection(SOD) a deep learning model 

### Download the model (Not Required - rembg automatically download it for us)
- https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx
- https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx
  


## How to run the FastAPI

1. Create a python virtual environment and activate it: 
   - python3 -m venv venv 
   - source venv/bin/activate

2. install all the required libraries using requirements.txt
   - pip install -r requirements.txt

3. run the API
   - python3 app.py

4. open url in the browser
   - http://127.0.0.1:8000/docs

5. upload the image (.jpg, .jpeg , .png) in FastAPI Swagger UI

6. we get the output as dict with base64 of the image




## For the demo purpose I create a Streamlit App

### How to run the Streamlit app

- go to the path where streamlit_app_demo.py is located and run the below command
- streamlit run streamlit_app_demo.py



## Other References

- Official repository of U-2-Net
  - https://github.com/xuebinqin/U-2-Net

## Reserch paper for the u2net

- U2-Net: Going Deeper with Nested U-Structure for Salient Object Detection
- https://arxiv.org/pdf/2005.09007.pdf


