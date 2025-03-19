import streamlit as st
from resume_parser import extract_text, preprocess
from ranking import rank_resumes
import streamlit as st
import nltk

# Download stopwords if not already present
nltk.download('stopwords')
nltk.download('punkt_tab')

# Streamlit UI
st.title("AI Resume Screening & Ranking System")
st.subheader("Upload Resumes and Get Ranked Based on Job Description")

# Job Description Input
job_desc = st.text_area("Paste Job Description Here")

# Upload Resumes
uploaded_files = st.file_uploader("Upload Resumes", accept_multiple_files=True, type=["pdf", "docx"])

# Process and Rank Resumes
if st.button("Start Screening") and job_desc:
    resume_texts = []
    for file in uploaded_files:
        text = extract_text(file)
        cleaned_text = preprocess(text)
        resume_texts.append(cleaned_text)

    results = rank_resumes(resume_texts, job_desc)

    # Display Rankings
    st.subheader("Ranked Candidates")
    for i, (text, score) in enumerate(results, 1):
        st.write(f"{i}. Score: {score:.2f}")
