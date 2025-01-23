from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_list.html', {'resumes': resumes})

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_list')  # Redirecionar para a lista de resumes
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})