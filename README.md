# 🍽️ Daily Dish AI Chatbot

🔗 **Live Demo:** https://daily-dish-chatbot-alxehdxvrvkgwvrghncxfb.streamlit.app/

## 📌 Overview

Daily Dish AI Chatbot is an advanced AI-powered restaurant customer support assistant built using a **Multi-Agent RAG (Retrieval-Augmented Generation) Architecture**.

The chatbot uses:

* Semantic Search
* Sentence Transformer Embeddings
* FAISS Vector Database
* Conversational Memory

to retrieve accurate answers from restaurant FAQ documents and provide fast, reliable customer support.

---

## 🚀 Features

✅ Multi-Agent AI Workflow
✅ Semantic Search Retrieval
✅ FAISS Vector Database
✅ Sentence Transformer Embeddings
✅ Conversational Memory
✅ Streamlit Chat Interface
✅ PDF-Based Knowledge Retrieval
✅ Real-Time User Interaction
✅ Low-Latency Response System
✅ CI/CD Pipeline using GitHub Actions

---

## 🧠 Multi-Agent Architecture

The chatbot follows a four-stage AI workflow:

### 1️⃣ Query Understanding Agent

* Cleans and processes user queries
* Extracts useful keywords
* Normalizes text input

### 2️⃣ Document Retrieval Agent

* Converts queries into embeddings
* Searches FAQ knowledge base using FAISS
* Retrieves the most relevant FAQ response

### 3️⃣ Memory Agent

* Maintains conversation history
* Stores previous interactions
* Supports contextual responses

### 4️⃣ Response Generation Agent

* Formats chatbot responses
* Filters low-confidence matches
* Returns final user-friendly answers

---

## 🏗️ System Architecture

```text
User Query
    ↓
Query Understanding Agent
    ↓
Document Retrieval Agent
    ↓
Memory Agent
    ↓
Response Generation Agent
    ↓
Final Response
```

---

## 🛠️ Technologies Used

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Core Backend         |
| Streamlit             | Web Interface        |
| Sentence Transformers | Semantic Embeddings  |
| FAISS                 | Vector Database      |
| PyPDF2                | PDF Processing       |
| NumPy                 | Numerical Operations |
| NLP                   | Query Understanding  |
| GitHub Actions        | CI/CD Pipeline       |

---

## 📂 Project Structure

```text
Daily-Dish-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── The-Daily-Dish-FAQ.pdf
│
├── assets/
│   ├── chatbot-ui.png
│   └── architecture.png
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Anuj2606/Daily-Dish-Chatbot.git
cd Daily-Dish-Chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🧪 Example Questions

* What are your opening hours?
* Do you offer home delivery?
* Can I reserve a table for 10 people?
* Do you have vegan options?
* Do you host private events?

---

## 📸 Screenshots

*Add chatbot screenshots and architecture images inside the assets folder.*

---

## 🔮 Future Improvements

* LLM-based Response Generation
* Voice Assistant Integration
* Multilingual Support
* Real-Time Reservation System
* Cloud Database Integration
* Advanced Conversational Memory
