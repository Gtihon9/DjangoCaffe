from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('map/', views.map, name='map'),
    path('<int:pk>', views.detail_view, name='detail'),
    path('', TemplateView.as_view(template_name='moth_site/hello.html'), name='hello'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
