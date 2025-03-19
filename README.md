## 📄 **README.md** - AI-Powered Resume Screening and Ranking System  
---
# **AI-Powered Resume Screening and Ranking System**  
🚀 An AI-driven application that screens and ranks resumes based on their relevance to a given job description. Built using **Streamlit**, **scikit-learn**, **NLTK**, and **SpaCy** to streamline the recruitment process and enhance candidate selection.  

---

## **📁 Project Overview**
The AI-Powered Resume Screening System helps recruiters efficiently screen and rank resumes based on a job description. The system uses **Natural Language Processing (NLP)** techniques to preprocess resumes and rank them based on their relevance using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## **🛠️ Features**
- Upload multiple resumes in **PDF** or **DOCX** format.  
- Enter a job description to rank candidates.  
- View ranked candidates based on relevance scores.  
- User-friendly **Streamlit** interface.  
- Efficient text extraction, preprocessing, and similarity analysis.

---

## **📂 Folder Structure**
```
AIRESUME/
│── app.py                    # Streamlit app
│── ranking.py                # Resume ranking logic
│── resume_parser.py          # Text extraction and preprocessing
│── requirements.txt          # Required libraries
│── README.md                 # Project documentation (this file)
│── sample_resumes/           # Folder for sample resumes (PDF/DOCX)
```

---

## **🔧 Technologies Used**
- **Streamlit**  
- **scikit-learn**  
- **NLTK**  
- **SpaCy**  
- **PyPDF2**  
- **python-docx**

---

## **🚀 Getting Started**
### **1. Clone the Repository**
```bash
git clone https://github.com/ThatiShraddha/AI-Powered-Resume-Screening.git
cd AI-Powered-Resume-Screening
```

### **2. Create and Activate Virtual Environment**  
**For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
nltk.download('punkt')
nltk.download('stopwords')
```

### **4. Run the Streamlit App**
```bash
streamlit run app.py
```
- The app will open in your browser at **http://localhost:8501/**.

---

## **📝 Usage Instructions**
1. Paste a **Job Description** in the input box.  
2. Upload multiple resumes in **PDF** or **DOCX** format.  
3. Click on **Start Screening** to rank the resumes.  
4. View ranked candidates based on relevance scores.  

---

## **📊 Example Output**
**Job Description:**  
*Looking for a data scientist experienced in Python and machine learning.*

**Ranked Candidates:**  
1. **Score:** 0.85 - [Candidate 1]  
2. **Score:** 0.72 - [Candidate 2]  
3. **Score:** 0.60 - [Candidate 3]

---

## **📦 Requirements**
- Streamlit  
- NLTK  
- SpaCy  
- scikit-learn  
- PyPDF2  
- python-docx  
---

## **🌐 Deployment on Streamlit Cloud**
1. Ensure all code is pushed to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Connect your GitHub account and select this repository.  
4. Set **app.py** as the entry point.  
5. Deploy and share your live app link!  

---

## **👥 Contributing**
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the app.  

---

## **📄 License**
This project is licensed under the **MIT License**.  

---

## **💬 Contact**
For any questions or feedback:  
[ThatiShraddha](https://github.com/ThatiShraddha)

---

🎉 **Thank you for using the AI-Powered Resume Screening System!**  
If you found this project helpful, please ⭐ the repository!

---

If you need any adjustments or further details, feel free to ask! 😊🚀
