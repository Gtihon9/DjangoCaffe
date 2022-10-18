from django.template.defaulttags import url
from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('', include('caffes.urls')),
    path('', TemplateView.as_view(template_name='moth_site/hello.html'), name='hello'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
