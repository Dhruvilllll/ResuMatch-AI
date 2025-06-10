# 📄 AI Resume Analyzer & Job Match Predictor

A Streamlit-based application that uses OpenAI's GPT model to evaluate resumes against job descriptions and provide smart recommendations, match scores, and improvement tips.

---

## 🚀 Features

- Upload a **Resume (PDF)** and a **Job Description (PDF or TXT)**
- Extract and display raw text from documents
- Use OpenAI GPT to:
  - Analyze skill match
  - Highlight missing skills
  - Suggest improvements
  - Return an overall job match score
- Compute **Cosine Similarity** using TF-IDF
- Fully built using **Streamlit**, **LangChain-ready**, and **OpenAI API**

---

## 🧰 Tech Stack

| Area                | Tool/Library           |
|---------------------|------------------------|
| UI & Deployment     | Streamlit              |
| LLM Integration     | OpenAI API             |
| PDF Parsing         | PyMuPDF                |
| NLP/Scoring         | Scikit-learn, NLTK     |
| Prompt Management   | Custom + LangChain     |
| Deployment          | Streamlit Cloud        |

---

## 🛠️ Setup Instructions

### 1. Clone the repo

git clone https://github.com/yourusername/resume-analyzer.git<br/>
cd resume-analyzer

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add OpenAI API Key

#### Create a .env file and add:
OPENAI_API_KEY=your-openai-key-here

#### In app.py, load it using:<br/>

from dotenv import load_dotenv <br/>
import os<br/>
load_dotenv()<br/>
openai.api_key = os.getenv("OPENAI_API_KEY")


### 4. Run the App

streamlit run app.py
