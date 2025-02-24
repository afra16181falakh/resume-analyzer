import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag, ne_chunk

# NLTK data downloads are handled externally

def extract_name(resume_text):
    """Extract candidate name from resume text"""
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(resume_text)
    words = [word for word in words if word.isalpha() and word not in stop_words]
    tagged_words = pos_tag(words)
    named_entities = ne_chunk(tagged_words, binary=False)
    
    for subtree in named_entities:
        if isinstance(subtree, nltk.Tree) and subtree.label() == 'PERSON':
            return ' '.join([leaf[0] for leaf in subtree.leaves()])
    return None

def extract_skills(resume_text):
    """Extract skills from resume text"""
    skills = []
    skill_keywords = [
        "python", "java", "machine learning", "data analysis", "javascript", "c++", 
        "project management", "artificial intelligence", "natural language processing"
    ]
    words = word_tokenize(resume_text.lower())
    
    for skill in skill_keywords:
        if skill in ' '.join(words):
            skills.append(skill)
    
    return list(set(skills))

def analyze_resume(resume_text):
    """Analyze resume and extract key information"""
    return {
        "name": extract_name(resume_text),
        "skills": extract_skills(resume_text),
        "education": extract_education(resume_text),
        "experience": extract_experience(resume_text)
    }

def extract_education(resume_text):
    """Extract education information from resume text"""
    education_keywords = [
        "Bachelor", "Master", "PhD", "degree", "University", "College", "Institute"
    ]
    education_info = []
    for line in resume_text.splitlines():
        if any(keyword in line for keyword in education_keywords):
            education_info.append(line.strip())
    return education_info if education_info else "No education information found."

def extract_experience(resume_text):
    """Extract work experience from resume text"""
    experience_keywords = [
        "worked at", "experience", "internship", "role", "position", "employed", "was a"
    ]
    experience_info = []
    for line in resume_text.splitlines():
        if any(keyword in line.lower() for keyword in experience_keywords):
            experience_info.append(line.strip())
    return experience_info if experience_info else "No experience information found."
