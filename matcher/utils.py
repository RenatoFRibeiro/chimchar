import spacy
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def extract_relevant_details(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    print("The doc has the following elements:", doc)
    
    skills = []
    experience = []
    education = []

    # Usar expressões regulares para identificar seções
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
