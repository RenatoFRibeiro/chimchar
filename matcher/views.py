from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume, JobOpening
from .utils import extract_text_from_pdf, extract_relevant_details, compare_resume_with_jobs
from .serializers import JobOpeningSerializer
from rest_framework import viewsets

class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer

def homepage(request):
    return render(request, 'homepage.html')

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            pdf_path = resume.file.path
            extracted_text = extract_text_from_pdf(pdf_path)
            details = extract_relevant_details(extracted_text)
            resume.skills = ', '.join(details['skills'])
            resume.experience = ', '.join(details['experience'])
            resume.education = ', '.join(details['education'])
            resume.save()
            return redirect('matched_jobs', resume_id=resume.id)  # Redirecionar para a nova view
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})

def matched_jobs(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    results = compare_resume_with_jobs(resume)
    return render(request, 'matched_jobs.html', {'resume': resume, 'results': results})

def job_openings(request):
    job_openings = JobOpening.objects.all()
    return render(request, 'job_openings.html', {'job_openings': job_openings})