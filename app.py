# app.py

import streamlit as st
from dotenv import load_dotenv
import os
import openai

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.scorer import calculate_match_score
from prompts.prompt_templates import resume_analysis_prompt

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit page config
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("📄 AI Resume Analyzer & Job Match Predictor")

st.markdown("Upload your **Resume** and a **Job Description**, and let AI analyze the match!")

# File Uploads
resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("📄 Upload Job Description (PDF or .txt)", type=["pdf", "txt"])

# Extracted text placeholders
resume_text = ""
jd_text = ""

# Extract resume text
if resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    resume_text = clean_text(resume_text)
    st.subheader("📘 Extracted Resume Text:")
    st.text_area("Resume", resume_text, height=300)

# Extract JD text
if jd_file:
    if jd_file.name.endswith(".pdf"):
        jd_text = extract_text_from_pdf(jd_file)
    else:
        jd_text = jd_file.read().decode()
    jd_text = clean_text(jd_text)
    st.subheader("📄 Extracted Job Description Text:")
    st.text_area("Job Description", jd_text, height=300)

# Analyze button
if st.button("🔍 Analyze Resume"):
    if resume_text and jd_text:
        with st.spinner("Analyzing with AI..."):

            # 1. LLM Analysis
            prompt = resume_analysis_prompt(resume_text, jd_text)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            gpt_result = response["choices"][0]["message"]["content"]

            # 2. Cosine Similarity Score
            match_score = calculate_match_score(resume_text, jd_text)

            # 3. Display Results
            st.success("✅ Analysis Complete!")
            st.markdown(f"### 📊 TF-IDF Match Score: `{match_score}%`")
            st.markdown("---")
            st.markdown("### 🤖 GPT-4 Analysis:")
            st.markdown(gpt_result)

    else:
        st.warning("Please upload both Resume and Job Description to proceed.")
