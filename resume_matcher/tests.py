from django.test import TestCase
from django.urls import reverse
from .models import JobPosting, Resume
from .utils import process_resume, match_resume_with_jobs
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

class ResumeMatcherTests(TestCase):
    def setUp(self):
        # Create test job postings
        self.job1 = JobPosting.objects.create(title="Software Engineer", description="Python, Django, REST API")
        self.job2 = JobPosting.objects.create(title="Data Scientist", description="Python, Machine Learning, SQL")
        
        # Sample resume file
        self.resume_content = "I am proficient in Python and Django."
        self.resume_file = SimpleUploadedFile("resume.txt", self.resume_content.encode())

    def test_upload_resume(self):
        url = reverse('upload-resume')
        response = self.client.post(url, {'file': self.resume_file})
        self.assertEqual(response.status_code, 200)
        self.assertIn('resume_id', response.data)

    def test_match_results(self):
        # Create a resume
        resume = Resume.objects.create(file=self.resume_file)

        # Test utility function directly
        match_results = match_resume_with_jobs(resume, JobPosting.objects.all())
        self.assertEqual(len(match_results), 2)  # Two job postings
        self.assertGreater(match_results[0]['match_percentage'], 0)

    def test_process_resume(self):
        # Test resume processing function
        processed_data = process_resume(BytesIO(self.resume_content.encode()))
        self.assertIn("Python", processed_data['skills'])
