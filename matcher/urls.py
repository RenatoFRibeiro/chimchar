from django.urls import path, include
from .views import upload_resume, resume_list
from rest_framework.routers import DefaultRouter
from .views import JobOpeningViewSet

router = DefaultRouter()
router.register(r'job_openings', JobOpeningViewSet)

urlpatterns = [
#    path('upload/', upload_resume, name='upload_resume'),
    path('', upload_resume, name='upload_resume'),  # URL padrão para upload
    path('resumes/', resume_list, name='resume_list'),  # URL para listar os resumes
    path('', include(router.urls)), # URL padrão para listar os job_openings
]

