import os
import openai
import pandas as pd
import numpy as np
import faiss
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Absolute path to the prompt file
prompt_path = os.path.join(script_dir, "py_prompt.txt")

# Function to load the prompt from a file
def load_prompt(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    print("Loading prompt:", file_path)
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Load the structured prompt
structured_prompt = load_prompt(prompt_path)

# Absolute path to the CSV file
adaptabrasil_filepath = os.path.join(script_dir, "Base de Riscos do Adapta Brasil.csv")

# Prepare for RAG if data is loaded
if os.path.exists(adaptabrasil_filepath):
    print("Processing database")

    # Load data from CSV
    df = pd.read_csv(adaptabrasil_filepath, encoding='utf-8')

    # Combine relevant content into a list of texts
    documents = df.apply(lambda row: ' '.join(row.astype(str)), axis=1).tolist()

    # Get embeddings for each document
    print("Obtaining document embeddings")
    embeddings = []
    batch_size = 100  # Adjust based on your API rate limits
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i+batch_size]
        response = openai.Embedding.create(
            input=batch,
            engine='text-embedding-ada-002'
        )
        batch_embeddings = [data["embedding"] for data in response["data"]]
        embeddings.extend(batch_embeddings)

    embeddings = np.array(embeddings).astype('float32')

    # Build the FAISS index
    print("Building FAISS index")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    print(f"Total vectors indexed: {index.ntotal}")

    print("Database processed")
else:
    index = None
    documents = None
    embeddings = None

# Function to retrieve documents based on a query
def retrieve_documents(query, top_k=5):
    if index is None:
        return []

    # Get embedding for the query
    response = openai.Embedding.create(
        input=[query],
        engine='text-embedding-ada-002'
    )
    query_embedding = np.array(response['data'][0]['embedding']).astype('float32')

    # Search for the most similar documents
    D, I = index.search(np.array([query_embedding]), top_k)
    retrieved_texts = [documents[i] for i in I[0]]
    return retrieved_texts

# Function to run the chatbot with RAG
def run_resiliencIA():
    print("Iniciando ResiliêncIA. Digite 'sair' para encerrar a conversa.")

    history = [
        {"role": "system", "content": structured_prompt},
        {"role": "user", "content": ""}
    ]
    # Initial assistant message
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=history,
        temperature=0,
    )
    assistant_reply = response['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": assistant_reply})
    print(f"ResiliêncIA: {assistant_reply}")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("ResiliêncIA: Obrigado por usar a ferramenta. Até logo!")
            break

        history.append({"role": "user", "content": user_input})

        # Retrieve relevant documents if necessary
        retrieved_texts = retrieve_documents(user_input)
        if retrieved_texts:
            context = "\n".join(retrieved_texts[:3])  # Use top 3 documents
            # Add context as a system message
            context_message = {"role": "system", "content": f"Informações adicionais para auxiliar na resposta:\n{context}"}
            messages = history + [context_message]
        else:
            messages = history

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
        )
        assistant_reply = response['choices'][0]['message']['content']
        history.append({"role": "assistant", "content": assistant_reply})

        print(f"ResiliêncIA: {assistant_reply}")

if __name__ == "__main__":
    run_resiliencIA()
