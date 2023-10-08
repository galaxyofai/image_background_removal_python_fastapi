import streamlit as st



from src import with_rembg
from datetime import datetime

import os

def main():
    st.title("Image Background Removal")

    # Sidebar
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Image Background Removal"))

    if page == "Home":
        st.write("Welcome to the Image Background Removal App.")
        st.write("Upload an image, and we'll remove the background for you.")

    elif page == "Image Background Removal":
        model_type=st.radio("Model name", ("u2net", "u2netp"))
        if model_type=="u2net":
            model_type="1"
        if model_type=="u2netp":
            model_type="2"
        img_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if img_file:
            today_date = str(datetime.now().date())
            current_time = str(datetime.now().strftime("%H_%M_%S"))
            print(img_file.type)
            # Image extension validation
            if img_file.type.startswith('image/'):
                # Give input and output file names
                 #give input and output file names
                file_save_path="./images/uploaded_images/"+today_date+"/"+current_time+"_"+img_file.name
                file_output_path="./images/removed_bg/"+today_date+"/"+current_time+"_removed_bg_"+img_file.name
                filename=current_time+"_removed_bg_"+img_file.name
                 # Check images directory exists or not, if not then create.
                if not os.path.exists(f"./images/uploaded_images/{today_date}/"):
                    os.makedirs(f"./images/uploaded_images/{today_date}/")

                # Check removed_bg directory exists or not, if not then create.
                if not os.path.exists(f"./images/removed_bg/{today_date}/"):
                    os.makedirs(f"./images/removed_bg/{today_date}/")


                if '.jpg' or '.jpeg' in filename.lower():
                    fname,fextension=os.path.splitext(filename)
                    filename=filename.replace(fextension,".png")
                print(filename)
               

                # Save uploaded file into the directory
                with open(file_save_path, "wb") as f:
                    f.write(img_file.read())

                # Check if the file is successfully saved and exists on the given path or not
                if os.path.exists(file_save_path):
                    result = with_rembg.remove_background(file_save_path, file_output_path,model_type)
                    
                    if result['status'] == "success":

                        st.image(result['file_out_path'], use_column_width=True)
                        st.success("Image saved successfully.")
                        with open(result['file_out_path'], "rb") as file:
                            file_contents = file.read()
                        st.download_button(label="Download Image",data=file_contents,file_name=filename)
                    else:
                        st.error("Image not saved.")
                else:
                    st.error("Image not saved.")

            else:
                st.error("File type is not valid. Please upload only jpg, jpeg, and png.")

if __name__ == "__main__":
    main()
