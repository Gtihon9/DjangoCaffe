from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', TemplateView.as_view(template_name='moth_site/home.html'), name='home'),
    path('users/', include('users.urls')),
    path(r'^i18n/', include('django.conf.urls.i18n')),
    path('', include('moth_site.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
