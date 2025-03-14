import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv
import google.generativeai as genai


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## function to load the gemini pro model and get response

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history = [])

def get_gemini_response(question):
    resopnse = chat.send_message(question, stream = True)
    return resopnse

## intialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application ")

## Intilizae the session sytate for chat history if it doesn't exist 

if 'chat_history' not in st.session_stae:
    st.session_state['chat_history'] = []

input = st.text_input('Input', key = 'input')
submit = st.button("Ask the question")


if submit and input:
    response = get_gemini_response(input)
    ## ad dthe user query and response to session chat history 

    st.session_state['chat_history'].append(("you", input))
    st.subheader(" The Response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheaer("The chat history is ")

for role, text in st.sessionn_state['chat_history']:
    st.write(f'{role}:{text}')