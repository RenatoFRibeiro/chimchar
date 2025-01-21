# Resume Matcher Backend Challenge

## Overview
The **Resume Matcher Backend Challenge** is a backend application designed to match resumes against job postings. It provides REST API endpoints for uploading resumes, processing them, and generating matching results based on job requirements.

The application leverages **Django** and **Django REST Framework (DRF)** for backend functionality and uses **spaCy** for natural language processing (NLP) to analyze and compare resumes with job descriptions.

## Features
- **Upload Resumes**  
  Users can upload resumes (e.g., `.txt` or `.pdf`) that are processed and stored in the database.

- **Job Posting Management**  
  Add job descriptions to the database to define matching criteria.

- **Resume Matching**  
  - Match Percentage: Calculate alignment between a resume and a job posting.
  - Skill Alignment: Identify overlapping skills between resumes and job descriptions.
  - Skill Gaps: Highlight skills required by the job but missing in the resume.

- **GraphQL API**  
  Retrieve job postings via GraphQL queries.

- **Dockerized Deployment**  
  Includes a Dockerfile for containerized deployment.

- **Automated Testing**  
  Comprehensive test coverage using Django's `unittest`.

## Technologies Used
- **Frameworks**: Django, Django REST Framework
- **NLP Library**: spaCy
- **Database**: SQLite (default for Django)
- **Containerization**: Docker
- **Testing**: Django's `unittest`, coverage
- **GraphQL**: graphene-django

## Project Structure

```markdown
backend_challenge/
│
├── backend_challenge/       # Main Django project folder
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL routing
│   └── ...
│
├── resume_matcher/          # App for resume matching
│   ├── models.py            # Database models
│   ├── views.py             # API views
│   ├── utils.py             # Utility functions for processing resumes
│   ├── urls.py              # URL routing for the app
│   ├── graphql.py           # GraphQL schema
│   ├── tests.py             # Unit tests
│   └── ...
│
├── db.sqlite3               # Database file
├── manage.py                # Django management script
├── Dockerfile               # Dockerfile for containerization
├── requirements.txt         # Python dependencies
└── README.md                # Documentation
```

# Installation and Setup

## Clone the Repository
```markdown
git clone https://github.com/RenatoFRibeiro/chimchar.git
cd backend_challenge
```

## Set Up a Virtual Environment
```markdown
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows
```
## Install Dependencies
```markdown
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
## Run Database Migrations
```markdown
python manage.py makemigrations
python manage.py migrate
```
## Run the Development Server
```markdown
python manage.py runserver
```
## Access the Application

REST API: http://127.0.0.1:8000/api/
Admin Panel: http://127.0.0.1:8000/admin/
API Endpoints
1. Upload Resume
```markdown
Endpoint: POST /api/upload-resume/
Payload: File upload (file key in form-data)
Response:
{
  "message": "Resume uploaded successfully!",
  "resume_id": 1
}
. Get Match Results
Endpoint: GET /api/match-results/<resume_id>/
Response:
[
  {
    "job_title": "Backend Developer",
    "match_percentage": 75.0,
    "alignment_details": "Matched skills: Python, Django",
    "gap_details": "Missing skills: REST API"
  }
]
```
## GraphQL Query (Job Postings)
```markdown
Endpoint: POST /graphql/
Example Query:
query {
  jobPostings {
    title
    description
  }
}
```
# Run Tests

## Run Unit Tests
```markdown
python manage.py test
```
## Generate Test Coverage Report
```markdown
coverage run manage.py test
coverage report
```
# Run with Docker

## Build Docker Image
```markdown
docker build -t resume-matcher .
```
## Run Docker Container
```markdown
docker run -p 8000:8000 resume-matcher
```
# Future Improvements

Enhance NLP capabilities with custom spaCy models.
Add support for parsing PDF resumes.
Improve matching algorithms to account for synonyms and proficiency levels.
Build a frontend for users to upload resumes and view results.