import streamlit as st  #Web App
import easyocr as ocr  #OCR
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("Easy OCR - Extract Text from Images")

st.markdown(
    """
<style>
    .css-18ni7ap.ezrtsby2 {
        display: none
    }

    .css-h5rgaw.ea3mdgi1 {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("Processing"):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.success("Here you go!")
    
else:
    st.write("Upload an Image")
