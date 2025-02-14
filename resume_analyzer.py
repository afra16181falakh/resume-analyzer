import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

def extract_name(resume_text):
    """Extract candidate name from resume text"""
    doc = nlp(resume_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(resume_text):
    """Extract skills from resume text"""
    skills = []
    doc = nlp(resume_text)
    matcher = Matcher(nlp.vocab)
    
    # Define skill patterns
    patterns = [
        [{"LOWER": "python"}],
        [{"LOWER": "java"}],
        [{"LOWER": "machine"}, {"LOWER": "learning"}],
        [{"LOWER": "data"}, {"LOWER": "analysis"}]
    ]
    
    matcher.add("SKILLS", patterns)
    matches = matcher(doc)
    
    for match_id, start, end in matches:
        skills.append(doc[start:end].text)
    
    return list(set(skills))

def analyze_resume(resume_text):
    """Analyze resume and extract key information"""
    return {
        "name": extract_name(resume_text),
        "skills": extract_skills(resume_text)
    }
