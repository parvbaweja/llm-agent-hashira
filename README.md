# 🤖 LLM Research Assistant with LangChain + FAISS

This project is a Retrieval-Augmented Generation (RAG) pipeline built using **LangChain**, **FAISS**, and **OpenAI** APIs. It lets you ask natural questions about any document and get accurate, context-aware answers.

---

## 🚀 Features

- 📄 Loads academic or plain-text documents
- 🔍 Splits and indexes data using **FAISS**
- 🧠 Uses **LangChain** to chain retrieval with LLM generation
- 🤖 Answers queries using **OpenAI** (or Hugging Face embeddings)
- 🔐 API key stored securely via `.env` (excluded from Git)

---

## 🛠️ Technologies Used

- Python 3
- LangChain
- FAISS
- OpenAI API / Hugging Face Transformers
- Dotenv

---

## 📂 Project Structure

```bash llm-agent-hashira/ ├── main.py ├── sample.txt ├── .env ├── .gitignore └── README.md ```

## 📦 Setup Instructions

```bash
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1    # For Windows PowerShell

# Install dependencies
pip install -r requirements.txt
# (or manually)
pip install langchain faiss-cpu langchain-community langchain-openai python-dotenv
 ```
Create a .env file:

OPENAI_API_KEY=your-key-here

💡 How It Works
Loads your sample.txt file

Splits text into chunks

Embeds them using OpenAIEmbeddings or HuggingFaceEmbeddings

Stores vectors in FAISS

Uses LangChain's RetrievalQA to find relevant chunks and generate an answer

✨ Example Output
Ask a question about the document: What is LangChain?

Answer: LangChain is a framework for building LLM-powered apps.

🧪 Demo & Use Cases
Chat with PDFs or academic papers
Fine-tune for resume screening
Extend with Streamlit UI for deployment

📄 License
MIT License
