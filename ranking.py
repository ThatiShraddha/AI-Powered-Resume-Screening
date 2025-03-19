from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_texts, job_description):
    """
    Rank resumes based on similarity to the job description.

    Args:
        resume_texts (list of str): List of cleaned resume texts.
        job_description (str): The job description text.

    Returns:
        list of tuple: Each tuple contains (resume_text, similarity_score).
    """
    # Combine job description and resumes for vectorization
    documents = [job_description] + resume_texts

    # Create a TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Compute cosine similarity between the job description (index 0) and all resumes
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Pair each resume with its corresponding similarity score
    ranked_results = sorted(zip(resume_texts, similarity_scores), key=lambda x: x[1], reverse=True)

    return ranked_results
