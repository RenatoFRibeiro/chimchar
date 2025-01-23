from django.contrib import admin
from django.urls import path, include
from matcher.views import upload_resume
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('matcher.urls')),  # Inclua as URLs da app matcher
    path('', RedirectView.as_view(url='/upload/', permanent=True)),  # Redireciona a URL raiz para /upload/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


