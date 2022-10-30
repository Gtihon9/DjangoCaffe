from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.create_map, name='map'),
    path('', include('caffes.urls')),
    path('', TemplateView.as_view(template_name='moth_site/hello.html'), name='hello'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
