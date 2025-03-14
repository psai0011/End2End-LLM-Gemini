from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Funtion to load the gemini pro model and get responses
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input, image):
    if input!="":
 
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
        
    return response.text


# intializa the streamlit app

st.set_page_config(page_title = "Gemini Image Demo")

st.header (" Gemini LLM application ")
input = st.text_input("Input prompt: ", key= "input")

upload_file = st. file_uploader(" choose an image ......", type=["jpg","jpeg", "png"])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption = " Upload Image ", use_column_width=True)


sumbit = st.button("Tell me about the image")

## if submit clicked
if sumbit:
    response = get_gemini_response(input, image)
    st.subheader("The Respnose is ")
    st.write(response)
