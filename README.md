# rag-llm-chatbot

# Setup

# Create .env file in root directory
OPENAI_API_KEY=<YOUR_API_KEY> \\
PINECONE_API_KEY=<YOUR_API_KEY>

# Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Launch Backend Server
uvicorn run:app --host 0.0.0.0 --port 8000 --reload

# Launch Frontend Webpage
streamlit run webpage.py
