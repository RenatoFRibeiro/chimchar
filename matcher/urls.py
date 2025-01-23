from django.urls import path
from .views import upload_resume, resume_list

urlpatterns = [
#    path('upload/', upload_resume, name='upload_resume'),
    path('', upload_resume, name='upload_resume'),  # URL padrão para upload
    path('resumes/', resume_list, name='resume_list'),  # URL para listar os resumes
]