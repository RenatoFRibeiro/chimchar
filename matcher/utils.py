import spacy
import fitz  # PyMuPDF
import re
from .models import Resume, JobOpening

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def extract_relevant_details(text):
    skills = []
    experience = []
    education = []

    skills_section = re.search(r'Skills(.*?)(Experience|Education|$)', text, re.DOTALL | re.IGNORECASE)
    experience_section = re.search(r'Experience(.*?)(Skills|Education|$)', text, re.DOTALL | re.IGNORECASE)
    education_section = re.search(r'Education(.*?)(Skills|Experience|$)', text, re.DOTALL | re.IGNORECASE)

    if skills_section:
        skills_text = skills_section.group(1).strip()
        skills = [skill.strip() for skill in skills_text.split(',')]

    if experience_section:
        experience_text = experience_section.group(1).strip()
        experience = [exp.strip() for exp in experience_text.split(',')]

    if education_section:
        education_text = education_section.group(1).strip()
        education = [edu.strip() for edu in education_text.split(',')]
    
    return {
        'skills': skills,
        'experience': experience,
        'education': education
    }

def calculate_match_percentage(resume, job_opening):
    resume_skills = set(re.findall(r'\b\w+\b', resume.skills.lower()))
    job_skills = set(re.findall(r'\b\w+\b', job_opening.skills_required.lower()))

    matching_skills = resume_skills.intersection(job_skills)
    total_skills = job_skills

    match_percentage = (len(matching_skills) / len(total_skills)) * 100 if total_skills else 0

    return match_percentage, matching_skills, total_skills - matching_skills


def compare_resume_with_jobs(resume):
    job_openings = JobOpening.objects.all()
    results = []

    for job in job_openings:
        match_percentage, matching_skills, missing_skills = calculate_match_percentage(resume, job)
        results.append({
            'job': job,
            'match_percentage': match_percentage,
            'matching_skills': matching_skills,
            'missing_skills': missing_skills
        })

    # Ordenar os resultados pela porcentagem de correspondência
    results.sort(key=lambda x: x['match_percentage'], reverse=True)

    return results