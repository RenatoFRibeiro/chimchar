from django.urls import path, include
from .views import upload_resume, resume_list, matched_jobs, homepage, job_openings
from rest_framework.routers import DefaultRouter
from .views import JobOpeningViewSet

router = DefaultRouter()
router.register(r'job_openings', JobOpeningViewSet)

urlpatterns = [
    #path('upload/', upload_resume, name='upload_resume'),
    path('', homepage, name='homepage'),  # Homepage
    path('upload/upload_resume', upload_resume, name='upload_resume'),  # URL padrão para upload
    path('resumes/', resume_list, name='resume_list'),  # URL para listar os resumes
    #path('', include(router.urls)), # URL padrão para listar os job_openings
    path('matched_jobs/<int:resume_id>/', matched_jobs, name='matched_jobs'),
    path('job_openings/', job_openings, name='job_openings'),  # List job openings
    path('job_manager/', JobOpeningViewSet.as_view({'post': 'list'}), name='job_manager'),  # List job openings

]
