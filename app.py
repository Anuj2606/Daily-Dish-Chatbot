%%writefile app.py

# ============================================================
# THE DAILY DISH — MULTI-AGENT RAG CHATBOT
# ============================================================

"""
============================================================
PROJECT OVERVIEW
============================================================

This chatbot uses an Advanced Multi-Agent RAG Architecture.

------------------------------------------------------------
AGENT 1 — QUERY UNDERSTANDING AGENT
------------------------------------------------------------
Responsibilities:
- Cleans user query
- Processes text
- Extracts keywords
- Normalizes input

------------------------------------------------------------
AGENT 2 — DOCUMENT RETRIEVAL AGENT
------------------------------------------------------------
Responsibilities:
- Uses semantic embeddings
- Uses FAISS vector database
- Searches FAQ PDF intelligently
- Retrieves exact FAQ answer

------------------------------------------------------------
AGENT 3 — MEMORY AGENT
------------------------------------------------------------
Responsibilities:
- Stores conversation history
- Maintains chatbot memory

------------------------------------------------------------
AGENT 4 — RESPONSE GENERATION AGENT
------------------------------------------------------------
Responsibilities:
- Generates final chatbot response
- Formats chatbot output
- Handles low-confidence queries

============================================================
TECHNOLOGIES USED
============================================================

- Python
- Streamlit
- Sentence Transformers
- FAISS Vector Database
- PyPDF2
- NLP
- Semantic Search
- RAG Architecture
- Multi-Agent Workflow
"""

# ============================================================
# IMPORT LIBRARIES
# ============================================================

import re
import faiss
import numpy as np
import streamlit as st

from PyPDF2 import PdfReader

from sentence_transformers import SentenceTransformer

# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

st.set_page_config(
    page_title="Daily Dish AI Chatbot",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ The Daily Dish AI Chatbot")

st.write(
    """
    Welcome to The Daily Dish AI Chatbot!

    Ask questions about:
    - Reservations
    - Delivery
    - Menu
    - Timings
    - Events
    - Restaurant information
    """
)

faq_pdf_path = "/content/drive/MyDrive/The_Daily_Dish_FAQ.pdf"

reader = PdfReader(faq_pdf_path)

full_text = ""

for page in reader.pages:

    text = page.extract_text()

    if text:
        full_text += text + "\n"

# ============================================================
# CLEAN TEXT FUNCTION
# ============================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r'\s+', ' ', text)

    return text

cleaned_text = clean_text(full_text)

# ============================================================
# CREATE FAQ QUESTION-ANSWER PAIRS
# ============================================================

faq_pairs = []

pattern = r'(\d+\.\s*q.*?a:.*?)(?=\d+\.\s*q|$)'

matches = re.findall(
    pattern,
    cleaned_text,
    re.DOTALL
)

for match in matches:

    faq_pairs.append(match.strip())

print("Total FAQ Pairs:", len(faq_pairs))

# ============================================================
# EMBEDDINGS
# ============================================================

faq_embeddings = model.encode(
    faq_pairs
)

faq_embeddings = np.array(
    faq_embeddings
).astype('float32')

# ============================================================
# CREATE FAISS VECTOR DATABASE
# ============================================================

dimension = faq_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(faq_embeddings)

# ============================================================
# AGENT 1 — QUERY UNDERSTANDING AGENT
# ============================================================

def query_understanding_agent(user_query):

    """
    Responsibilities:
    - Cleans user query
    - Extracts keywords
    - Normalizes input
    """

    cleaned_query = clean_text(user_query)

    keywords = cleaned_query.split()

    return {
        "cleaned_query": cleaned_query,
        "keywords": keywords
    }

# ============================================================
# AGENT 2 — DOCUMENT RETRIEVAL AGENT
# ============================================================

def retrieval_agent(processed_query):

    """
    Responsibilities:
    - Converts query into embeddings
    - Searches vector database
    - Retrieves exact FAQ answer
    """

    query_embedding = model.encode(
        [processed_query["cleaned_query"]]
    )

    query_embedding = np.array(
        query_embedding
    ).astype('float32')

    distances, indices = index.search(
        query_embedding,
        1
    )

    best_match_index = indices[0][0]

    best_distance = distances[0][0]

    retrieved_faq = faq_pairs[
        best_match_index
    ]

    return {
        "answer": retrieved_faq,
        "distance": best_distance
    }

# ============================================================
# AGENT 3 — MEMORY AGENT
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

def memory_agent(user_query, bot_response):

    """
    Responsibilities:
    - Stores conversation history
    - Maintains chatbot memory
    """

    st.session_state.messages.append({
        "role": "user",
        "content": user_query
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

# ============================================================
# AGENT 4 — RESPONSE GENERATION AGENT
# ============================================================

def response_generation_agent(retrieved_data):

    """
    Responsibilities:
    - Generates final chatbot response
    - Formats chatbot output
    - Handles irrelevant questions
    """

    distance = retrieved_data["distance"]

    # Lower distance = better match
    if distance > 0.9:

        return (
            "Sorry, I couldn't find relevant "
            "information related to your question."
        )

    answer = retrieved_data["answer"]

    # Extract only answer part
    answer_match = re.search(
        r'a:\s*(.*)',
        answer,
        re.DOTALL
    )

    if answer_match:

        final_answer = answer_match.group(1)

    else:

        final_answer = answer

    final_answer = re.sub(
        r'\s+',
        ' ',
        final_answer
    )

    final_answer = final_answer.strip()

    return final_answer.capitalize()

# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ============================================================
# USER INPUT
# ============================================================

user_query = st.chat_input(
    "Ask your question here..."
)

# ============================================================
# MAIN MULTI-AGENT WORKFLOW
# ============================================================

if user_query:

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_query)

    # ========================================================
    # AGENT 1 — QUERY UNDERSTANDING
    # ========================================================

    processed_query = query_understanding_agent(
        user_query
    )

    # ========================================================
    # AGENT 2 — DOCUMENT RETRIEVAL
    # ========================================================

    retrieved_data = retrieval_agent(
        processed_query
    )

    # ========================================================
    # AGENT 4 — RESPONSE GENERATION
    # ========================================================

    final_response = response_generation_agent(
        retrieved_data
    )

    # ========================================================
    # AGENT 3 — MEMORY STORAGE
    # ========================================================

    memory_agent(
        user_query,
        final_response
    )

    # ========================================================
    # DISPLAY FINAL RESPONSE
    # ========================================================

    with st.chat_message("assistant"):

        st.markdown(final_response)
