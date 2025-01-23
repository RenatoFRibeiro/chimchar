from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume, JobOpening
from .utils import extract_text_from_pdf, extract_relevant_details
from .serializers import JobOpeningSerializer
from rest_framework import viewsets


class JobOpeningViewSet(viewsets.ModelViewSet):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningSerializer

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
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})