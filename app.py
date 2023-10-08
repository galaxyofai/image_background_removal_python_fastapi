from fastapi import FastAPI,UploadFile, File
import uvicorn
import os 
from datetime import datetime
from src import with_rembg
import base64
app = FastAPI()

@app.get("/")
def hello():
    return {"API":"API is working fine"}

@app.post("/image_backgroung_remove")
async def upload_image(model_type:str ="1",img_file:UploadFile =File(...)):
    """
        Model Type: \n

        1 - U2net (175 MB) - This model is based on the U2-Net architecture, which is a deep neural network designed for salient object detection \n  

        2 - U2netp (4.7 MB) - It an improved version of U2-Net, designed to be more efficient and faster while maintaining good performance. \n
        \n\n
        Args: \n
            model_type (str): 1 or 2.\n
            img_file (File): uploaded image \n
    
        Returns: \n 
            dict: A dictionary containing the message and base64 of an image. \n
    """
    today_date=str(datetime.now().date())
  
    current_time=str(datetime.now().strftime("%H_%M_%S"))


    #image extension validation
    if '.jpg' in img_file.filename or '.jpeg' in img_file.filename or '.png' in img_file.filename:

        #give input and output file names
        file_save_path="./images/uploaded_images/"+today_date+"/"+current_time+"_"+img_file.filename
        file_output_path="./images/removed_bg/"+today_date+"/"+current_time+"_removed_bg_"+img_file.filename
        
        #check images directory exists or not, if not then create.
        if os.path.exists("./images/uploaded_images/"+today_date+"/") == False:
            os.makedirs("./images/uploaded_images/"+today_date+"/")

        #check removed_bg directory exists or not, if not then create.

        if os.path.exists("./images/removed_bg/"+today_date+"/") == False:
            os.makedirs("./images/removed_bg/"+today_date+"/")

        #save uploaded file into the directory
        with open(file_save_path, "wb") as f:
            f.write(img_file.file.read())

        #Check File is successfully saved and exists on the given path or not
        if os.path.exists(file_save_path):
            result=with_rembg.remove_background(file_save_path,file_output_path,model_type)
            
            if result['status'] == "success":
                # Open the PNG image file in binary mode
                with open(result['file_out_path'], 'rb') as image_file:
                    # Read the image data
                    image_data = image_file.read()

                # convert the image data in base64 format
                base64_encoded = base64.b64encode(image_data)
                return {"message": f"Image saved at {result['file_out_path']} successfully","status":"success","file_base64":base64_encoded}
            else:
                return {"error":result['error'],"status":"fail"}
        else:
            return {"error":"Image Not saved !!!","status":"fail"}
    else:
        return {"error": "File Type is not valid please upload only jpg,jpeg and png","status":"fail"}


if __name__=="__main__":
    uvicorn.run(app,)