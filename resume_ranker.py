from transformers import BertTokenizer, BertModel
import torch
import openai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

# Initialize BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embedding(text):
    """Generate BERT embedding for text"""
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()

def get_openai_embedding(text):
    """Generate OpenAI embedding for text"""
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return np.array(response['data'][0]['embedding'])
    except Exception as e:
        print(f"Error generating OpenAI embedding: {e}")
        return None

def rank_resumes(resumes, job_description):
    """Rank resumes based on similarity to job description"""
    # Get job description embedding
    job_embedding = get_bert_embedding(job_description)
    
    # Calculate similarity scores
    ranked_resumes = []
    for resume in resumes:
        resume_embedding = get_bert_embedding(resume)
        similarity = cosine_similarity(job_embedding, resume_embedding)[0][0]
        ranked_resumes.append({
            "resume": resume,
            "similarity_score": float(similarity)
        })
    
    # Sort by similarity score
    ranked_resumes.sort(key=lambda x: x['similarity_score'], reverse=True)
    return ranked_resumes

# Ensure OpenAI API key is set
openai.api_key = os.getenv('OPENAI_API_KEY')
