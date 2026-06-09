# 🩺 Medical Chatbot – GenAI Powered Healthcare Assistant

An AI-powered Medical Chatbot built using Generative AI and Retrieval-Augmented Generation (RAG) to provide accurate and context-aware responses to medical queries.

The chatbot leverages Large Language Models (LLMs), vector embeddings, and semantic search to retrieve relevant medical information from a curated knowledge base before generating responses.

> ⚠️ Disclaimer: This project is intended for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---

## Features

-  AI-powered conversational medical assistant
-  Retrieval-Augmented Generation (RAG)
-  Semantic search using vector embeddings
-  Medical PDF knowledge base ingestion
-  Context-aware question answering
-  User-friendly web interface
-  Fast document retrieval with vector database

---

## System Architecture

```text
Medical PDFs
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Embeddings Model
      │
      ▼
Vector Database
      │
      ▼
Retriever
      │
      ▼
Large Language Model (LLM)
      │
      ▼
Medical Chatbot Response
```

---

## Tech Stack

### Backend
- Python
- Flask
- LangChain
- Generative AI / LLMs

### AI & NLP
- Hugging Face Embeddings
- Retrieval-Augmented Generation (RAG)
- Semantic Search

### Vector Database
- Pinecone

### Deployment
- Docker
- AWS EC2
- GitHub Actions

---

## 📂 Project Structure

```text
Medical-Chatbot-Gen-AI/
│
├── Data/                   # Medical knowledge base
├── src/                    # Source code
├── static/                 # Static assets
├── templates/              # HTML templates
├── app.py                  # Main Flask application
├── store_index.py          # Vector database indexing
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
├── Dockerfile              # Docker configuration
├── .github/workflows/      # CI/CD workflows
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/BhargaviVyshnavi20/Medical-Chatbot-Gen-AI.git
cd Medical-Chatbot-Gen-AI
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

---

## 📚 Create Vector Index

Generate embeddings and store them in the vector database:

```bash
python store_index.py
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:5000
```

---

## 💡 How It Works

1. Medical documents are loaded into the system.
2. Documents are split into smaller chunks.
3. Each chunk is converted into embeddings.
4. Embeddings are stored in a vector database.
5. User queries are converted into embeddings.
6. Relevant document chunks are retrieved.
7. The LLM generates responses using retrieved context.
8. The chatbot returns accurate and context-aware answers.

---

## 📸 Demo

### Chat Interface
<img width="914" height="1280" alt="health assistant git image - 1" src="https://github.com/user-attachments/assets/bb615348-ab3d-4530-b0be-30bd4c78a35f" />
<img width="265" height="348" alt="image" src="https://github.com/user-attachments/assets/e79c294e-1364-4b58-bcb5-ccdc77980db7" />


---

## 🔮 Future Enhancements

- Voice-enabled conversations
- Multi-language support
- Medical report analysis
- Prescription understanding
- Appointment assistance
- Healthcare recommendation system






