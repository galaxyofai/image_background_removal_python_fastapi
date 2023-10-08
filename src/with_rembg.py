import rembg
from PIL import Image
import os
from rembg import new_session

def remove_background(image_path,output_path,model_type):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Remove the background 
        if model_type=="1":
            model_name="u2net"
        elif model_type == "2":
            model_name="u2netp"
        else:
            return {"error":"model type is not specified correctly use 1 - u2net and 2 - u2netp","status":"fail"}

        output = rembg.remove(image,session = new_session(model_name))
        fname,fextension=os.path.splitext(output_path)
        output_path=output_path.replace(fextension,".png")
        
        # Save the output image
        output.save(output_path,format="PNG")

        return {"status":"success","file_out_path":output_path}
    except Exception as e:
        return {"error":str(e),"message":"getting error in removing backgroung using rembg","status":"fail"}


