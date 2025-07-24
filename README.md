# 🧠 AI Resume Screening App

This is a lightweight AI-powered Resume Scanner using OpenAI's GPT + LangChain + Flask.  
It analyzes resumes (PDF/DOC/TXT), extracts text, compares with trending skills for a job role using RAG, and returns:
- ✅ Skill Match %
- ✅ Matched Skills
- ❌ Missing Trending Skills

### 🔧 Tech Stack
- Python (Flask API)
- LangChain + OpenAI GPT (RAG-based skill extraction)
- PyTesseract + PDF2Image + python-docx + PyPDF
- Google Colab (for backend)

### 📦 How to Use
1. Upload your resume file (`.pdf`, `.docx`, or `.txt`) and specify the job role.
2. App will return a skill match % and list of missing/matched skills.

---

### 🔗 Hosted on Colab + Flask + PyNgrok
This project runs locally using Flask & is exposed using `ngrok` to test API endpoints.

