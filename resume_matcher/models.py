from django.db import models

# Creating a model to import and store the resumes

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MatchResult(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    match_percentage = models.FloatField()
    alignment_details = models.TextField()
    gap_details = models.TextField()
