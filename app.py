from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## Funtion to load the gemini pro model and get responses
model = genai.GenerativeModel("gemma-3-27b-it")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
## intialize the streamlit app

st.set_page_config(page_title = "Q&A Demo" )
st.header("Gemini LLM Application")

input = st.text_input("Input : ", key = "input")

submit = st.button("Ask your question")


## when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)

