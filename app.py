from langchain_openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

def get_openai_response(prompt):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)
    response = llm.invoke(prompt)
    return response

st.set_page_config(page_title="QnA Demo", layout="wide")
st.header("QnA Demo")

input_text = st.text_input("Enter your question: ", key="input_text")
response = get_openai_response(input_text)

submit=st.button("Generate")

if submit:
    st.subheader("The response is")
    st.write(response)