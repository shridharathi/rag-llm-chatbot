# rag-llm-chatbot


Chat/query on text from any URL you want to upload.

This webapp was an exploration in self-implementing Retrival Augmented Generation (RAG) technology. The backend scrapes the text in the URL, chunks the text, embeds the chunks using OpenAI embeddings, and stores the embeddings in Pinecone. Then, the user can query about content in the webpage; this query is constructed into a prompt for GPT-4, and a similarity search is conducted within the Pinecone database to retreive the most relevant information/answer.



Setup:

Create .env file in root directory

`OPENAI_API_KEY=<YOUR_API_KEY>`

`PINECONE_API_KEY=<YOUR_API_KEY>`


Create Virtual Environment

`python3 -m venv venv`

`source venv/bin/activate`


Install Python dependencies

`pip install -r requirements.txt`


Launch Backend Server

`uvicorn run:app --host 0.0.0.0 --port 8000 --reload`


Launch Frontend Webpage

`streamlit run webpage.py`

