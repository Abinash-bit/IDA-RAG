# 📄 Document Q&A Application

This application lets you ask questions about various documents—like Word, PowerPoint, Excel, and Emails—and get intelligent answers sourced directly from the content using **Google Vertex AI's Gemini Pro** and **ChromaDB** for semantic retrieval.

---

## 🚀 Features

- ✅ Supports `.docx`, `.pptx`, `.xlsx`, `.msg`, and `.eml` file formats  
- 🤖 Embeds content using **Vertex AI's `text-embedding-large`** model  
- 💬 Answers questions via **Gemini 1.5 Pro (via Vertex AI)**  
- 🔍 Retrieves relevant document segments using **ChromaDB**  
- 🔗 Provides clickable source links with confidence scores  
- 🖥️ Clean and interactive UI using **Streamlit**

---

## 🛠️ Setup Instructions

```bash
1. git clone https://github.com/your-username/document-qa-app.git
   cd document-qa-app

2. conda create -n qa-llm python=3.10 -y
   conda activate qa-llm

3. pip install -r requirements.txt

streamlit
chromadb
openpyxl
python-docx
python-pptx
extract-msg
pandas
email
vertexai
google-cloud-aiplatform

https://cloud.google.com/sdk/docs/install
gcloud auth application-default login
import vertexai
vertexai.init(project="your-project-id", location="us-central1")


QA_LLM/
├── data/
│   ├── docx/      # .docx files
│   ├── pptx/      # .pptx files
│   ├── excel/     # .xlsx files
│   ├── email/     # .msg files
│   └── gmail/     # .eml files
├── app.py
├── ingest.py
├── question_answering.py
├── generate_embeddings.py
├── chroma_store/
├── README.md
├── requirements.txt

python ingest.py
streamlit run app.py
