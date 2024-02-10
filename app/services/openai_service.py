import requests
import json
import os
from openai import OpenAI
from app.utils.helper_functions import construct_messages_list, build_prompt

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
#openai_client = OpenAI(api_key=OPENAI_API_KEY)

OPENAI_EMBEDDING_MODEL = 'text-embedding-ada-002'
PROMPT_LIMIT = 3750
CHATGPT_MODEL = 'gpt-4-1106-preview'

def get_embedding(chunk):
  url = 'https://api.openai.com/v1/embeddings'
  headers = {
      'content-type': 'application/json; charset=utf-8',
      'Authorization': f"Bearer {OPENAI_API_KEY}"            
  }
  data = {
      'model': OPENAI_EMBEDDING_MODEL,
      'input': chunk
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))  
  response_json = response.json()
  embedding = response_json["data"][0]["embedding"]
  # response = openai_client.embeddings.create(
  #     input=chunk, model=OPENAI_EMBEDDING_MODEL)
  # embedding = response.data[0].embedding
  return embedding


def get_llm_answer(prompt):
  """
  messages = [{"role": "system", "content": "You are a helpful assistant."}]
  # Pass in the entire chat history

  for message in chat_history:
    if message['isBot']:
      messages.append({"role": "system", "content": message["text"]})
    else:
      messages.append({"role": "user", "content": message["text"]})

  # Replace last message with the full prompt
  messages[-1]["content"] = prompt

  url = 'https://api.openai.com/v1/chat/completions'
  headers = {
      'content-type': 'application/json; charset=utf-8',
      'Authorization': f"Bearer {OPENAI_API_KEY}"            
  }
  data = {
      'model': CHATGPT_MODEL,
      'messages': messages,
      'temperature': 1, 
      'max_tokens': 1000
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))
  response_json = response.json()
  completion = response_json["choices"][0]["message"]["content"]
  return completion
  """
  messages = [{"role": "system", "content": "You are a helpful assistant."}]
  messages.append({"role": "user", "content": prompt})
  # Send the payload to the LLM to retrieve an answer
  url = 'https://api.openai.com/v1/chat/completions'
  headers = {
      'content-type': 'application/json; charset=utf-8',
      'Authorization': f"Bearer {OPENAI_API_KEY}"            
  }
  data = {
      'model': CHATGPT_MODEL,
      'messages': messages,
      'temperature': 1, 
      'max_tokens': 1000
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))
  
  # return the final answer
  response_json = response.json()
  completion = response_json["choices"][0]["message"]["content"]
  completion.replace("\n", "")
  return completion

def construct_llm_payload(question, context_chunks, chat_history):
  
  # Build the prompt with the context chunks and user's query
  prompt = build_prompt(question, context_chunks)
  print("\n==== PROMPT ====\n")
  print(prompt)

  # Construct messages array to send to OpenAI
  messages = construct_messages_list(chat_history, prompt)

  # Construct headers including the API key
  headers = {
      'content-type': 'application/json; charset=utf-8',
      'Authorization': f"Bearer {OPENAI_API_KEY}"            
  }  

  # Construct data payload
  data = {
      'model': CHATGPT_MODEL,
      'messages': messages,
      'temperature': 1, 
      'max_tokens': 1000,
      'stream': True
  }

  return headers, data
