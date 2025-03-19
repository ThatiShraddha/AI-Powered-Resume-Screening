import PyPDF2
import docx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Extract text from PDF/DOCX
def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        pdf = PyPDF2.PdfReader(file)
        text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = " ".join([para.text for para in doc.paragraphs])
    return text

# Preprocess text (remove stopwords, tokenize)
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered = [word.lower() for word in tokens if word.isalpha() and word not in stop_words]
    return " ".join(filtered)
