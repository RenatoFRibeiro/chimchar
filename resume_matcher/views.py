from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from .models import Resume

# Creating my views here, starting with the REST code related to the API

class ResumeUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        resume = Resume.objects.create(file=file_obj)
        return Response({"success": True, "resume_id": resume.id})
