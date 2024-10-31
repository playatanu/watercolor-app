import streamlit as st
from streamlit_image_comparison import image_comparison
from water_color import watercolor_effect
from PIL import Image
import tempfile

st.set_page_config(page_title="Image to Water color Image", layout="centered")
st.markdown('# Image to Water color Image')

uploaded_file = st.file_uploader("")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
        image_path = temp_file_path
        
        image = Image.open(temp_file_path)
        
        image_comparison(
        img1=image,
        img2=watercolor_effect(image,sigma_s=1,filter_n=10),
        label1="Original Image",
        label2="Water Color Image",
        width=700,
        in_memory = True,
        show_labels=True,
        make_responsive=True,
        
        
        )
        
        