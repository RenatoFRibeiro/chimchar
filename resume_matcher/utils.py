import spacy
from .models import MatchResult

nlp = spacy.load("en_core_web_sm")

def process_resume(file_path):
    # Extract resume details using NLP
    with open(file_path, 'r') as f:
        content = f.read()
    doc = nlp(content)
    skills = [ent.text for ent in doc.ents if ent.label_ in ['SKILL', 'LANGUAGE']]
    return {"skills": skills}

def match_resume_with_jobs(resume, job_postings):
    resume_details = process_resume(resume.file.path)
    results = []
    for job in job_postings:
        job_doc = nlp(job.description)
        job_keywords = [ent.text for ent in job_doc.ents if ent.label_ in ['SKILL', 'LANGUAGE']]
        matched_skills = set(resume_details["skills"]) & set(job_keywords)
        match_percentage = len(matched_skills) / len(job_keywords) * 100
        alignment_details = f"Matched skills: {', '.join(matched_skills)}"
        gap_details = f"Missing skills: {', '.join(set(job_keywords) - set(resume_details['skills']))}"
        results.append({
            "job_title": job.title,
            "match_percentage": match_percentage,
            "alignment_details": alignment_details,
            "gap_details": gap_details
        })
    return results
