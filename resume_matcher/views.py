from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Resume, JobPosting, MatchResult
from .utils import process_resume, match_resume_with_jobs

class ResumeUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        resume = Resume.objects.create(file=file_obj)
        resume.save()
        return Response({'message': 'Resume uploaded successfully!', 'resume_id': resume.id})

class MatchResultsView(APIView):
    def get(self, request, resume_id, *args, **kwargs):
        resume = Resume.objects.get(id=resume_id)
        job_postings = JobPosting.objects.all()
        match_results = match_resume_with_jobs(resume, job_postings)
        return Response(match_results)
