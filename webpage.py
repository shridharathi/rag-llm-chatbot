import streamlit as st
import requests
import json

BACKEND_URL = "http://localhost:8000"  # Replace with your actual backend URL

def embed_and_store_url(url):
    response = requests.post(f"{BACKEND_URL}/embed-and-store", params={"url": url})
    if response.status_code == 200:
        st.write("Embedding and storing successful!")
    else:
        st.write(f"Error: {response.status_code}")

def handle_query(question):
    response = requests.post(f"{BACKEND_URL}/handle-query", params={"question": question})
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.text}"

def delete_index():
    response = requests.post(f"{BACKEND_URL}/delete-index")
    if response.status_code == 200:
        st.write("Index deleted successfully!")
    else:
        st.write(f"Error: {response.status_code}")


st.write("# Welcome to URL Assistant! 👋")

st.write(
    "Hi! I'm your URL-specific assistant.\n I can answer any question you have about text from any URL.")

url = st.text_input("Enter a URL: ")

if st.button("Embed URL", key="url"):
    embed_and_store_url(url)


question = st.chat_input("Enter a question:")
chat_history = []

if question:
    with st.chat_message("user"):
        st.markdown(question)
    with st.spinner("..."):
        response = handle_query(question)
        with st.chat_message("assistant"):
            st.write(response.replace('\n', ''))
    chat_history.append({"isBot": False, "text": question}) 
    chat_history.append({"isBot": True, "text": response})

if st.button("End session", key="final"):
    delete_index()
